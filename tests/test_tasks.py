from dongfeng_base.tasks.misc import get_ip, get_resource_usage


def test_get_ip():
    assert isinstance(get_ip(), str)


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
