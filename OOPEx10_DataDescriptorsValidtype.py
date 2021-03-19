class ValidType:
    def __init__(self, type_):
        self._type = type_

    def __set_name__(self, cls, prop_name):
        self.prop_name = prop_name

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f"Value is not correct type, {self._type.__name__}")
        instance.__dict__[self.prop_name] = value
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

import numbers

class Person:
    age = ValidType(int)
    height = ValidType(numbers.Real)
    tags = ValidType(list)

p1 = Person()
p1.age = 10
p1.height = 182
p1.tags = [1,2,3]

print(p1.__dict__)

# try:
#     p1.age = 10.0
# except ValueError as ex:
#     print(ex)