import math

class Circle:
    def __init__(self, R):
        self._r = R
        self._area = None

    @property
    def radius(self):
        return self._r
    
    @radius.setter
    def radius(self, R):
        if R < 0:
            raise ValueError('Cant set < 0')
        self._r = R
        self._area = None
    
    @radius.deleter
    def radius(self):
        del self._r

    @property
    def area(self):
        if self._area is None:
            print('Calculating area')
            self._area = math.pi * (self.radius ** 2)
        return self._area

c = Circle(2)
# print(c.radius)
# print(c.area)
c.radius = 5
print(c.radius)
print(c.area)
print(c.area)
c.radius = 8
print(c.radius)
print(c.area)
print(c.area)
print(c.__dict__)
delattr(c, 'radius')
print(c.__dict__)