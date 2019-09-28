import ipaddress

from dongfeng_base.utils.ip import is_ip, is_cidr, is_private_ip, parse_ips, get_ip
from dongfeng_base.utils.worker import get_resource_usage


class TestIP(object):
    def test_get_ip():
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
    def test_get_resource_usage():
        result = get_resource_usage()
        assert isinstance(result.ip, str)
        assert isinstance(result.hostname, str)
        assert result.uptime > 0.0
        assert result.cpu > 0.0
        assert result.worker_cpu >= 0.0
        assert result.mem > 0.0
        assert result.worker_mem > 0.0
        assert result.worker_threads >= 1
