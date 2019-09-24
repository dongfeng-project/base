from enum import Enum, unique


@unique
class TaskName(Enum):
    @unique
    class OverWatch(Enum):
        GET_WORKER_STATS = "overwatch.misc.get_worker_stats"
