class Mod:
    def __init__(self, value, modulus):
        if modulus <= 0 and not isinstance(modulus, int):
            raise ValueError('Modulus cannot be less than 0')
        
        if not isinstance(value,int):
            raise TypeError('Value must be INT')

        self._modulus = modulus
        self._value = value % modulus 
    
    @property
    def value(self):
        return self._value
    
    @property
    def modulus(self):
        return self._modulus

    def __repr__(self):
        return f"Mod object, Value={self.value}, Modulus={self.modulus}"
    
    def __str__(self):
        return f"Mod object, Value={self.value}, Modulus={self.modulus}"
    
    def __add__(self, other):
        if isinstance(other, Mod) and (self.modulus == other.modulus):
            adder = self._value + other._value
            return Mod(adder, self.modulus)
        elif isinstance(other, int):
            adder = self._value + other
            return Mod(adder, self.modulus)
        else:
            raise NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, Mod) and (self.modulus == other.modulus):
            adder = self._value + other._value
            return Mod(adder, self.modulus)
        elif isinstance(other, int):
            adder = self._value + other
            return Mod(adder, self.modulus)
        else:
            raise NotImplemented

    def __eq__(self, other):
        if isinstance(other, Mod) and (self.modulus == other.modulus):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            raise NotImplemented
    
    def __int__(self):
        return self.value

m1 = Mod(10,4)
m2 = Mod(10,4)

print(m1==m2)
# print(m1+5)
# m1 += 3
# m1 += m2
# print(m1)
# print(int(m1))
print(int(m1))