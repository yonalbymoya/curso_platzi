import unittest
from src.bank_account import BankAccount
import os

class BankAccountTest(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual.")
    
    def test_withdrew(self):
        new_balance = self.account.withdrew(200)
        self.assertEqual(new_balance, 800,"El balance no es 200")

    def test_balance(self):
        self.assertEqual(self.account.get_balance(), 1000,"El balance no es igual")
        
    def test_trasnsaction_log(self):
        new_balance = self.account.deposit(500)
        os.path.exists("transaction_log.txt")
        self.assertTrue(os.path.exists("transaction_log.txt"))
        
    def test_count_transaction(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2
    

