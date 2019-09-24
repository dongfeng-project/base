from enum import Enum, unique


@unique
class TaskQueue(Enum):
    OVERWATCH = "overwatch"
    SCOUT = "scout"
