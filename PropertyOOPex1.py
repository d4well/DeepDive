class Person:
    def __init__(self, name):
        self._name = name
    
    def set_name(self, name):
        print('Setting on')
        self._name = name
    
    def get_name(self):
        print('Get on')
        return self._name
    
    name = property(fget=get_name, fset=set_name)

p1 = Person('Zbyszek')
print(p1.name)
p1.name = 'Janek'
print(p1.name)
print(p1.__dict__)
print(Person.__dict__)
