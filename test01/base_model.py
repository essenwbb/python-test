from abc import abstractmethod
import time


class BaseModel:
    _subclass_basename = ''

    def __init__(self):
        pass

    @property
    def name(self):
        return self._subclass_basename[:-3]

    @abstractmethod
    def init_subclass_basename(self):
        pass

    def __call__(self, *args, **kwargs):
        self.init_subclass_basename()
        return self.name
