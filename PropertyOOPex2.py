class Person:
    prop = property(doc='Write-only property')

    @prop.setter
    def prop(self, value):
        self._name = value

class Person2:
    def prop_set(self, name):
        self._name = name
    
    prop = property(fset=prop_set, doc="Write-only property")  


p1 = Person()
p1.prop = 'Janek'
print(p1.__dict__)
# print(p1.prop)

p2 = Person2()
p2.prop = 'Zbyszek'
print(p2.__dict__)
print(p2.prop)