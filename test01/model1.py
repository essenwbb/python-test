from test01.base_model import BaseModel


class Model1(BaseModel):
    def init_birth(self):
        # Do something init _birth, eg: We only give it an initial value(my birth year).
        self._birth = 1994
