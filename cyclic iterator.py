class CyclIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(self.iterable)
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            item = next(self.iterator)
        finally:
            return item

cyclic = CyclIterator('abc')
for i in range(10):
    print(i, next(cyclic))
print('-'*20)
import itertools

cyclic2 = itertools.cycle('abc')
for i in range(10):
    print(i, next(cyclic2))