from aenum import Enum, unique


@unique
class TaskQueue(Enum):
    BASE = "base"
    OVERWATCH = "overwatch"
    SCOUT = "scout"
    MISSILE = "missile"
