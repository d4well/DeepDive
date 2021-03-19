
import math

class Polygon:
    def __init__(self, edges, radius):
        if edges < 3:
            raise ValueError
        else:
            self.edges = edges
            self.radius = radius

    def edges(self):
        return self.edges

    def internal_angle(self):
        result = (self.edges - 2)*(180/self.edges)
        return result
    
    def edge_len(self):
        edge_lenght = 2 * self.radius * math.sin(math.pi/self.edges)
        return edge_lenght

    def apothem(self):
        apothem = self.radius * math.cos(math.pi/self.edges)
        return apothem

    def area(self):
        area = 0.5*self.edges*self.edge_len()*self.apothem()
        return area
    
    def perimeter(self):
        return self.edge_len()*self.edges

    def area_peri_ratio(self):
        ratio = self.area() / self.perimeter()
        return ratio

    def __repr__(self):
        return f"Polygon made of {self.edges} edges and R={self.radius}"

    def __eq__(self, other):
        if isinstance(other, Polygon):
            return self.edges == other.edges
        else:
            return f"Must be polygon class"

    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.edges > other.edges
        else:
            return f"Must be polygon class"

class PolygonSeq:
    def __init__(self, *polys):
        if polys:
            self.polygons = [*polys]
        else:
            self.polygons = []

    def pop(self, i):
        return self.polygons.pop(i)

    def append(self, i):
        self.polygons.append(i)
        self.polygons.sort(key=lambda x: x.area_peri_ratio(),reverse=True)
    
    def __getitem__(self, i):
        return self.polygons[i]

    def __len__(self, i):
        return len(self.polygons)

    def max_efficient(self):
        return self.polygons[0]

    def __repr__(self) -> str:
        return f"Polygon sequence made of {self.polygons}"


p1 = Polygon(6,5)
p2 = Polygon(5, 6)

print(p1)
print(p1.area())

print(p1 < p2)

seq1 = PolygonSeq(p1,p2)
print(seq1)
p3 = Polygon(10,10)
p4 = Polygon(15,8)
p5 = Polygon(30,30)
seq1.append(p5)
seq1.append(p3)
seq1.append(p4)
for i in seq1:
    print(i.area_peri_ratio())
    print(i)

print(seq1.max_efficient())
print(seq1)