from time import sleep

class Profiler:
    def __init__(self, fn):
        self.counter = 0    
        self.fn = fn
    
    def __call__(self, *args, **kwargs):
        self.counter += 1
        result = self.fn(*args, **kwargs)
        return result

@Profiler
def func1_(a,b):
    return a*b

print(func1_(2,3))
print(func1_.counter)
