import os
import socket
import time

import psutil

from dongfeng_base.serializers.misc import ResourceSerializer
from dongfeng_base.utils.ip import get_ip


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
