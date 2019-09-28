from dongfeng_base.serializers import BaseSerializer


class ResourceSerializer(BaseSerializer):
    def __init__(
        self,
        ip: str = "127.0.0.1",
        hostname: str = "",
        uptime: float = 0.0,
        cpu: float = 0.0,
        worker_cpu: float = 0.0,
        mem: float = 0.0,
        worker_mem: float = 0.0,
        worker_threads: int = 1,
    ):
        self.ip = ip
        self.hostname = hostname
        self.uptime = uptime
        self.cpu = cpu
        self.worker_cpu = worker_cpu
        self.mem = mem
        self.worker_mem = worker_mem
        self.worker_threads = worker_threads
