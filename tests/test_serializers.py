from dongfeng_base.serializers import BaseSerializer


def test_baseserializer():
    base_serializer = BaseSerializer()
    assert "{" in str(base_serializer)
