import ipaddress


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
