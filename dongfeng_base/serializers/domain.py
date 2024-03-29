import datetime
from typing import List

from dongfeng_base.serializers import TaskResultSerializer
from dongfeng_base.serializers.host import UpHostsSerializer


class SubDomainSerializer(TaskResultSerializer):
    def __init__(self, subdomain: str, ip: list, corp_id: int, env: int, last_scan_time: datetime.datetime):
        super().__init__(env=env, last_scan_time=last_scan_time)
        self.subdomain = subdomain
        self.resolve_ip = UpHostsSerializer(up_hosts=ip, corp_id=corp_id, env=env, last_scan_time=last_scan_time)
        self.corp_id = corp_id

    @property
    def ip(self):
        return self.resolve_ip.up_hosts


class EnumSubDomainSerializer(TaskResultSerializer):
    def __init__(
        self, domain: str, env: int, last_scan_time: datetime.datetime, subdomain_list: List[SubDomainSerializer] = None
    ):
        super().__init__(env=env, last_scan_time=last_scan_time)
        self.domain = domain
        self.subdomain_list = subdomain_list if subdomain_list else None


class SubDomainTitleSerializer(TaskResultSerializer):
    def __init__(
        self,
        subdomain: str,
        title: str,
        status_code: int,
        content: str,
        env: int,
        last_scan_time: datetime.datetime,
        is_match: bool = False,
    ):
        super().__init__(env=env, last_scan_time=last_scan_time)
        self.subdomain = subdomain
        self.status_code = int(status_code)
        self.title = title
        self.content = content
        self.is_match = is_match
