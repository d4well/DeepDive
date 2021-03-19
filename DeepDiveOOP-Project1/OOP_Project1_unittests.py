from OOP_Project1 import BankAccount
import unittest


class TestAccount(unittest.TestCase):

    def test_create_account(self):
        acc_number = '123'
        first_name = 'First'
        last_name = 'Last'
        a1 = BankAccount(acc_number, first_name, last_name)
        self.assertEqual('123', a1.account_number)
        self.assertEqual(first_name, a1.first_name)
        self.assertEqual(last_name, a1.last_name)
    
    def test_error_check(self):
        acc_number = '123'
        first_name = 'First'
        last_name = 'Last'
        a1 = BankAccount(acc_number, first_name, last_name, start_balance=100)

        with self.assertRaises(ValueError):
            a1.withdraw(500)
    
    def test_transaction_code(self):
        acc_number = '123'
        first_name = 'First'
        last_name = 'Last'
        a1 = BankAccount(acc_number, first_name, last_name, start_balance=100)
        d1 = a1.deposit(100)
        self.assertIn('D-', d1)
        self.assertTrue(d1.startswith('D-'))
            

if __name__ == "__main__":
    unittest.main()