class ValidString:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be an str')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'{self.property_name} should be longer')
        instance.__dict__[self.property_name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)

class Person:
    name = ValidString(1)

p1 = Person()
p2 = Person()
p1.name = 'Zbyszek'
p2.name = 'Janek'
print(p1.__dict__)
print(p2.__dict__)
print(Person.name.__dict__)