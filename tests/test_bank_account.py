import unittest, os
from unittest.mock import patch
from src.exceptions import InsufficientFundsError
from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit_increases_balance_by_deposit_amount(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El balance no es igual")

    @patch("src.bank_account.datetime")
    def test_withdraw_decreases_balance_by_withdraw_amount(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El balance no es igual")

    def test_get_balance_returns_current_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit_logs_transaction(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_withdraw_logs_each_transaction(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)

    @patch("src.bank_account.datetime")
    def test_withdraw_raises_error_when_insufficient_funds(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        self.account.withdraw(100)

    def test_deposit_multiple_ammounts(self):
        test_cases = [
            {"ammount": 100, "expected": 1100},
            {"ammount": 3000, "expected": 4000},
            {"ammount": 4500, "expected": 5500}
        ]

        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transactions.txt")
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])

