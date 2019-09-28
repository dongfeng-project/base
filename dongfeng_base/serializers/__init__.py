class BaseSerializer(object):
    def __str__(self):
        return str(self.__dict__)

    __repr__ = __str__
