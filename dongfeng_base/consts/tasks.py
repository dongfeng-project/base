from aenum import Enum, unique, skip


@unique
class TaskName(Enum):
    @skip
    @unique
    class OverWatch(Enum):
        GET_WORKER_STATS = "overwatch.misc.get_worker_stats"
        RESOURCE_USAGE = "resource_usage"

    @skip
    @unique
    class Scout(Enum):
        DISCOVER_HOST = "scout.discover_host"
        DISCOVER_PORT = "scout.discover_port"
        DISCOVER_SERVICE = "scout.discover_service"
