import ipaddress
import json
import socket
from typing import List

import requests
from celery.utils.log import get_task_logger

from .. import exceptions

logger = get_task_logger(__name__)


def get_ip() -> str:
    """
    获取本机ip
    :return: ip
    """
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception as e:
        logger.error(f"获取本机IP异常 {e}", exc_info=True)
        return ""


def is_private_ip(string: str) -> bool:
    """
    判断是否内网ip
    :param string:
    :return: Bool
    """
    try:
        ip = ipaddress.ip_address(string.strip())
        return ip.is_private
    except ValueError:
        return False


def is_ip(string: str) -> bool:
    """
    判断是否ip
    :param string:
    :return:
    """
    try:
        # 判断 python 版本
        ipaddress.ip_address(string.strip())
        return True
    except ValueError:
        return False


def is_cidr(string: str) -> bool:
    """
    判断是否CIDR
    :param string:
    :return:
    """
    try:
        ipaddress.ip_network(string.strip())
        return True
    except ValueError:
        return False


def get_geo_location(ip: str) -> str:
    """
    获取IP地理位置
    :param ip:
    :return:
    """
    if not is_ip(ip):
        raise exceptions.InvalidIP(ip=ip)

    try:
        req = requests.get(url=f"http://freeapi.ipip.net/{ip}")
        if req.status_code == 200:
            try:
                result = req.json()
                return " ".join(result)
            except json.JSONDecodeError:
                logger.error(f"freeapi.ipip.net查询失败，响应内容 {req.text}")
                return ""
        else:
            logger.error(f"请求ipip.net失败，状态码 {req.status_code}，响应内容 {req.text}")
            return ""
    except Exception as e:
        logger.exception(f"请求ipip.net异常 {e}")
        return ""


def parse_ips(ips: str) -> List[ipaddress.ip_network]:
    """
    解析IP段字符串，返回切片的CIDR
    :param ips:
    :return:
    """
    ip_list = []

    if "-" in ips:
        # IP段
        start_ip_str, end_ip_str = ips.split("-")[:2]
        if not is_ip(start_ip_str) or not is_ip(end_ip_str):
            raise exceptions.InvalidIP(ip=ips)

        start_ip = ipaddress.ip_address(start_ip_str)
        end_ip = ipaddress.ip_address(end_ip_str)
        ip_list.extend([ipaddress.ip_address(int_ip) for int_ip in range(int(start_ip), int(end_ip) + 1)])

    elif "/" in ips:
        # CIDR
        if not is_cidr(ips):
            raise exceptions.InvalidCIDR(cidr=ips)

        cidr_network = ipaddress.ip_network(ips)

        ip_list.extend(list(cidr_network.hosts()))

    else:
        if not is_ip(ips):
            raise exceptions.InvalidIP(ip=ips)

        ip_list.append(ipaddress.ip_address(ips))

    ip_list = list(set(ip_list))
    start_ip = min(ip_list)
    end_ip = max(ip_list)

    cidr_list = []
    for addr in ipaddress.summarize_address_range(start_ip, end_ip):
        try:
            cidr_list.extend(addr.subnets(new_prefix=16))
        except ValueError:
            cidr_list.append(addr)

    return cidr_list
