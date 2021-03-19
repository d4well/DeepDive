# class IntegerValue:
#     def __init__(self):
#         self.instances = {}

#     def __set__(self, instance, value):
#         self.instances[instance] = int(value)

#     def __get__(self, instance, owner_class):
#         if instance is None:
#             return self
#         return self.instances.get(instance)
# import weakref

# class IntegerValue:
#     def __init__(self):
#         self.instances = weakref.WeakKeyDictionary()

#     def __set__(self, instance, value):
#         self.instances[instance] = int(value)

#     def __get__(self, instance, owner_class):
#         if instance is None:
#             return self
#         return self.instances.get(instance)

import weakref

class IntegerValue:
    def __init__(self):
        self.instances = {}

    def __set__(self, instance, value):
        self.instances[id(instance)] = (weakref.ref(instance, self._remove_obj), int(value))

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self.instances[id(instance)][1]

    def _remove_obj(self, weak_ref):
        reverse_lookup = [key for key, value in self.instances.items() if value[0] is weak_ref]
        if reverse_lookup:
            key = reverse_lookup[0]
            del self.instances[key]

class Point2D:
    x = IntegerValue()
    y = IntegerValue()

p1 = Point2D()
p2 = Point2D()

# print(p1)
p1.x = 100
p1.y = 200
# print(p1.__dict__)
# print(Point2D.__dict__)
# print(p1.y)
print(Point2D.x.__dict__)
del p1
print(Point2D.x.__dict__)
print(Point2D.y.__dict__)
