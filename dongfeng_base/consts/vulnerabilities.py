from aenum import Enum, unique


@unique
class VulnerabilityType(Enum):
    WEB = 0
    HOST = 1
