from dongfeng_base.serializers import BaseSerializer


class UpHostsSerializer(BaseSerializer):
    def __init__(self, up_hosts: list):
        self.up_hosts = up_hosts


class OpenPortsSerializer(BaseSerializer):
    def __init__(self, ip: str, ports: list):
        self.ip = ip
        self.open_ports = ports


class ServiceSerializer(BaseSerializer):
    def __init__(self, ip: str, port: int, service: str = "unknown", product: str = "", banner: str = ""):
        self.ip = ip
        self.port = port
        self.service = service
        self.product = product
        self.banner = banner
