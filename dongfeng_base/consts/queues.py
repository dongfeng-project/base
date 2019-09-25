from aenum import Enum, unique


@unique
class TaskQueue(Enum):
    OVERWATCH = "overwatch"
    SCOUT = "scout"
