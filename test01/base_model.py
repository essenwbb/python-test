from abc import abstractmethod
import time


class BaseModel:
    _birth = 0

    def __init__(self):
        pass

    @property
    def age(self):
        return time.localtime().tm_year - self._birth

    @abstractmethod
    def init_birth(self):
        pass

    def __call__(self, *args, **kwargs):
        self.init_birth()
        return self.age
