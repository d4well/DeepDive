class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        if self.fget is None:
            return AttributeError(f'{self.fget} is not specified')
        return self.fget(instance)
    
    def __set__(self, instance, value):
        if self.fset is None:
            return AttributeError(f"{self.fset} is not specified")
        self.fset(instance, value)

    def setter(self, fset):
        self.fset = fset
        return self

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @MakeProperty
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value

p1 = Person('Zbyszek', 10)
print(p1.__dict__)
p1.age = 20
print(p1.__dict__)    