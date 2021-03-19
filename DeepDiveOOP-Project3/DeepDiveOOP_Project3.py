from typing import Type


class Resource:
    def __init__(self, name, manufacturer, total):
        if not isinstance(name, str):
           raise TypeError("Name should be string")
        if not isinstance(manufacturer, str):
            raise TypeError("Manufacturer should be string")
        if not isinstance(total, int):
            raise TypeError("Total value must be int")
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = 0

    def _validation(self, n):
        if isinstance(n, int):
            return True
        else:
            raise TypeError("Value must be int")

    def claim(self, n):
        if self._validation(n) and self._total > n:
            self._total -= n
            self._allocated += n
        else:
            raise ValueError("Value cannot be larger than total \
                            ({self._total} < {n})")
    def freeup(self, n):
        if self._validation(n) and self._allocated >= n:
            self._total += n
            self._allocated -= n
        else:
            raise ValueError("Value cannot be larger than allocated \
                            ({self._allocated} < {n})")        
    
    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    def died(self, n):
        if self._validation(n) and (self.allocated >= n and self.total >= n):
            self._total -= n
            self._allocated -= n
        else:
            raise ValueError("Value cannot be larger than allocated and total")

    @property
    def available(self):
        return self._total - self._allocated

    def purchased(self, n):
        if self._validation(n):
            self._total += n
    
    @property
    def category(self):
        return f"Class name --> {type(self).__name__.lower()}"

    def __str__(self):
        return f"Name = {self._name}"

    def __repr__(self):
        return f"Debug repr: \
                total --> {self.total}, \
                manufacturer --> {self._manufacturer} \
                allocated --> {self._allocated}"

class CPU(Resource):
    def __init__(self, name, manufacturer, total, cores, socket, power_watts):
        super().__init__(name, manufacturer, total)
        if not isinstance(cores, int):
           raise TypeError("Cores should be int")
        if not isinstance(socket, str):
            raise TypeError("Socket should be string")
        if not isinstance(power_watts, int):
            raise TypeError("Power watts must be int")
        
        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        return self._cores

    @property
    def socket(self):
        return self._socket
    
    @property
    def power_watts(self):
        return self._power_watts
    
    def __repr__(self):
        return f"Debug CPU \
                cores --> {self.cores} \
                socket --> {self.socket} \
                power watts --> {self.power_watts} \
                total --> {self.total}, \
                manufacturer --> {self._manufacturer} \
                allocated --> {self._allocated}"

# cpu1 = CPU('AMD', 'AMD', 10, 50, 'AMD jakies', 150)
# print(repr(cpu1))
# cpu1.purchased(2)
# print(repr(cpu1))
# cpu1.claim(5)
# print(repr(cpu1))
# cpu1.died(5)
# print(repr(cpu1))