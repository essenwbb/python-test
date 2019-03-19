from test01.base_model import BaseModel
import os


class Model1(BaseModel):
    def init_subclass_basename(self):
        # Do something init _subclass_basename
        self._subclass_basename = os.path.basename(__file__)


if __name__ == '__main__':
    print()
    print(Model1()())
