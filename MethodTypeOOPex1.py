from types import MethodType

class Person:
    def __init__(self, name):
        self.name = name
    
    def register_do_work(self, func):
        setattr(self, '_do_work', MethodType(func, self))

    def do_work(self):
        do_work_func = getattr(self, '_do_work', None)
        if do_work_func:
            return do_work_func()
        else:
            raise AttributeError('Frist assign a func to obj')

def zbyszek_work(self):
    return f'{self.name} robi robote na budowie'

def mietek_work(self):
    return f'{self.name} robi robote na drodze'

p1 = Person('Zbyszek')
p2 = Person('Mietek')

p1.register_do_work(zbyszek_work)
p2.register_do_work(mietek_work)

print(p1.do_work())
print(p2.do_work())
