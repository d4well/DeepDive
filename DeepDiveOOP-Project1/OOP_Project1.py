import datetime
import numbers
import time

class BankAccount:
    _INTREST_RATE = 0.05

    def __init__(self, acc_number, first_name, last_name, time_offset=0, start_balance=0):
        self._acc_number = acc_number
        self._first_name = first_name
        self._last_name = last_name
        self.time_offset = time_offset
        self._balance = start_balance
        self._full_name = None
        self._transaction_id = 100
        self._transaction_code = None
        self._tansaction_time = None
        self._transactions_list = []

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = BankAccount.validate_name(first_name, 'First name')
        self._full_name = None
    
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = BankAccount.validate_name(last_name, 'Last name')
        self._full_name = None

    @property
    def full_name(self):
        if self._full_name is None:
            self._full_name = self.first_name + ' ' + self.last_name
        return self._full_name

    @staticmethod
    def validate_name(value, field_name) -> str:
        if value is None or len(str(value.strip())) == 0:
            raise ValueError(f'{field_name} cannot by empty')
        else:
            return str(value.strip())

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._acc_number

    def withdraw(self, value):
        self._transaction_id += 1
        if isinstance(value, numbers.Number) and self.balance >= value:
            self._balance -= value
            self._transaction_code = 'W'
            self._transaction_time = datetime.datetime.now()-datetime.timedelta(hours=self.time_offset)
            self.parse_confirmation()
        else:
            self._transaction_code = 'X'
            self._transaction_time = datetime.datetime.now()-datetime.timedelta(hours=self.time_offset)
            self.parse_confirmation()
            raise ValueError('Incorrect value or Value > Balance')

    def deposit(self, value):
        self._transaction_id += 1
        if isinstance(value, numbers.Number):
            self._balance += value
            self._transaction_code = 'D'
            self._transaction_time = datetime.datetime.now()-datetime.timedelta(hours=self.time_offset)
            return self.parse_confirmation()
        else:
            self._transaction_code = 'X'
            self._transaction_time = datetime.datetime.now()-datetime.timedelta(hours=self.time_offset)
            self.parse_confirmation()
            raise ValueError('Incorrect value')
        
    @classmethod
    def get_intrest_rate(cls):
        return cls._INTREST_RATE

    @classmethod
    def set_intrest_rate(cls, value):
        if isinstance(value,numbers.Real) and value > 0:
            cls._INTREST_RATE = value
            print("INTREST RATE HAS BEEN CHANGED")
        else:
            raise ValueError('Intrest rate must by number and > 0')

    def deposit_interest(self):
        self._transaction_id += 1
        self._balance = (self._balance * BankAccount.INTREST_RATE) + self._balance
        self._transaction_code = 'I'
        self._transaction_time = datetime.datetime.now()-datetime.timedelta(hours=self.time_offset)
        self.parse_confirmation()

    def parse_confirmation(self):
        self._info = f'{self._transaction_code}-{self._acc_number}-{self._transaction_time.strftime("%Y%m%d%H%M%S")}-{self._transaction_id}'
        self._transactions_list.append(self._info)
        # print(self._transactions_list)
        print(self._info)
        return self._info
    
    def confirmation_analys(self, confirmation):
        conf_info = confirmation.split('-')
        conf_type = conf_info[0]
        conf_acc = conf_info[1]
        conf_date = datetime.datetime.strptime(conf_info[2],"%Y%m%d%H%M%S")
        conf_id = conf_info[3]
        print(f"Type of transaction --> {conf_type}")
        print(f"Acc of transaction --> {conf_acc}")
        print(f"Date of transaction --> {conf_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"ID of transaction --> {conf_id}")
        return conf_info

    

# p1 = BankAccount(123,'Zbyszek','Kowalski', -1,1000)
# d1 = p1.deposit(100)
# print(d1)
# print(p1.balance)
# p1.withdraw(50)
# print(p1.balance)
# p1.confirmation_analys('D-123-20201231151808-1')
# p1.withdraw(1400)
