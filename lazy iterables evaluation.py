import math

class Cycle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area == None:
            print('Calculating area')
            self._area = math.pi * (self.radius**2)
        return self._area

c1 = Cycle(1)
print(c1.area)
c1.radius = 2
print(c1.area)
print(c1.area)