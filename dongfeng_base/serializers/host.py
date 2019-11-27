import datetime

from dongfeng_base.serializers import TaskResultSerializer


class UpHostsSerializer(TaskResultSerializer):
    def __init__(self, up_hosts: list, corp_id: int, env: str, last_scan_time: datetime.datetime):
        super().__init__(env=env, last_scan_time=last_scan_time)
        self.up_hosts = up_hosts
        self.corp_id = corp_id


class OpenPortsSerializer(TaskResultSerializer):
    def __init__(self, ip: str, ports: list, env: str, last_scan_time: datetime.datetime):
        super().__init__(env=env, last_scan_time=last_scan_time)
        self.ip = ip
        self.open_ports = ports


class ServiceSerializer(TaskResultSerializer):
    def __init__(
        self,
        ip: str,
        port: int,
        env: str,
        last_scan_time: datetime.datetime,
        service: str = "unknown",
        product: str = "",
        banner: str = "",
    ):
        super().__init__(env=env, last_scan_time=last_scan_time)
        self.ip = ip
        self.port = port
        self.service = service
        self.product = product
        self.banner = banner
