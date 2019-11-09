from dongfeng_base.serializers import BaseSerializer


class VulnerabilitySerializer(BaseSerializer):
    def __init__(self, code: str, description: str):
        self.code = code
        self.description = description
