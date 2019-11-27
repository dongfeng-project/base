import datetime


class BaseSerializer(object):
    def __str__(self):
        return str(self.__dict__)

    __repr__ = __str__


class TaskResultSerializer(BaseSerializer):
    def __init__(self, env: str, last_scan_time: datetime.datetime):
        self.env = env
        self.last_scan_time = last_scan_time
