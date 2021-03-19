class Person:
    def __init__(self, age):
        self._age = age
        self.age = 50

    def __getattr__(self, name):
        alt_name = '_' + name
        print(f"Could not find {name}, trying {alt_name}")
        
        try:
            return super().__getattribute__(alt_name)
        except AttributeError:
            return AttributeError(f"Could not find {alt_name}")

p = Person(60)
print(p.__dict__)
