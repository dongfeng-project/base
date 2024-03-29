import ipaddress

from dongfeng_base.utils.cmd import Command
from dongfeng_base.utils.hash import md5
from dongfeng_base.utils.ip import is_ip, is_cidr, is_private_ip, parse_ips, get_ip
from dongfeng_base.utils.worker import get_resource_usage


class TestIP(object):
    def test_get_ip(self):
        assert isinstance(get_ip(), str)

    def test_is_ip(self):
        assert is_ip("1.1.1.1") is True
        assert is_ip("abcdefg") is False

    def test_is_cidr(self):
        assert is_cidr("192.168.1.0/24") is True
        assert is_cidr("192.168.1.1/1234565") is False

    def test_is_private_ip(self):
        assert is_private_ip("192.168.1.1") is True
        assert is_private_ip("1.1.1.1") is False

    def test_parse_ips(self):
        assert ipaddress.ip_network("192.168.1.1/32") in parse_ips("192.168.1.1")
        assert ipaddress.ip_network("192.168.1.0/24") in parse_ips("192.168.1.0-192.168.2.1")
        assert ipaddress.ip_network("192.168.2.0/23") in parse_ips("192.168.0.0/16")
        assert ipaddress.ip_network("192.168.5.2/32") in parse_ips("192.168.5.2")


class TestWorker(object):
    def test_get_resource_usage(self):
        result = get_resource_usage()
        assert isinstance(result.ip, str)
        assert isinstance(result.hostname, str)
        assert result.uptime > 0.0
        assert result.cpu > 0.0
        assert result.worker_cpu >= 0.0
        assert result.mem > 0.0
        assert result.worker_mem > 0.0
        assert result.worker_threads >= 1


class TestHash(object):
    def test_md5(self):
        assert md5("0") == "cfcd208495d565ef66e7dff9f98764da"


class TestCmd(object):
    cmder = Command(timeout=5)

    def test_block_run(self):
        assert b"home" in self.cmder.run(cmd="ls -1 /", is_async=False)

    def test_async_run(self):
        for line in self.cmder.run(cmd="ls -1 /", is_async=True):
            assert b"\n" in line
