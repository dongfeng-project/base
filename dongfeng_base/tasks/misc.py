import os
import socket
import time

import psutil
from celery.utils.log import get_task_logger
from celery.worker.control import inspect_command

from ..consts.tasks import TaskName
from ..serializers.misc import ResourceSerializer

logger = get_task_logger(__name__)


@inspect_command(name=TaskName.OverWatch.RESOURCE_USAGE.value)
def resource_usage(state):
    result = get_resource_usage()
    return result.__dict__


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


def get_resource_usage() -> ResourceSerializer:
    """
    获取机器资源使用信息
    :return:
    """
    p = psutil.Process(os.getpid())
    with p.oneshot():
        worker_cpu = p.cpu_percent(interval=1)
        worker_mem = p.memory_info().rss / 1024 / 1024
        uptime = time.time() - p.create_time()
        agent_threads = p.num_threads()

    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent

    result = ResourceSerializer(
        ip=get_ip(),
        hostname=socket.gethostname(),
        uptime=uptime,
        cpu=cpu,
        worker_cpu=worker_cpu,
        mem=mem,
        worker_mem=worker_mem,
        worker_threads=agent_threads,
    )
    return result
