import time

birth = 1994

age = time.localtime().tm_year - birth

print(f'I born in {birth}, and I\'m {age} years old.')


import time


class Date:

    def __init__(self, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ['year', 'month', 'day']:
                    self.__setattr__(key, value)
        else:
            super().__init__()
            self.__dict__ = self.today().__dict__

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(year=t.tm_year, month=t.tm_mon, day=t.tm_mday)


if __name__ == '__main__':
    a = Date()
    print(a.__dict__)
    b = Date(year=2019, month=3, day=5)
    print(b.__dict__)
