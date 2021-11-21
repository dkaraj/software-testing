from python_unittest.bank import BankAccount
import unittest


class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Dori", 0, "$")

    def test_can_create_bank_account(self):
        self.assertTrue(isinstance(self.account, BankAccount))

    def test_balance(self):
        self.assertEqual(self.account.balance(), 0)

    def test_negative_initial_amount(self):
        with self.assertRaises(ValueError):
            BankAccount("Tester", -100, "$")

    def test_int_dunder(sefl):
        sefl.assertEqual(int(sefl.account), 0)

    def test_str_dunder(sefl):
        sefl.assertEqual(str(sefl.account), "Bank account for Dori with balance of 0$")

    def test_holder(self):
        account = BankAccount("Tester", 0, "$")
        self.assertEqual(account.holder(), "Tester")

    def test_currency(self):
        self.assertEqual(self.account.currency(), "$")

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance(), 100)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw_less_than_you_have(self):
        account = BankAccount("Tester", 100, "$")
        result = account.withdraw(20)

        self.assertTrue(result)
        self.assertEqual(account.balance(), 80)

    def test_withdraw_more_than_you_have(self):
        result = self.account.withdraw(50)
        self.assertIsNotNone(result)
        self.assertFalse(result)

    def test_transfer_to(self):
        account = BankAccount("Tester", 100, "$")
        result = account.transfer_to(self.account, 70)

        self.assertTrue(result)
        self.assertEqual(self.account.balance(), 70)
        self.assertEqual(account.balance(), 30)

    def test_history_when_account_is_created(self):
        self.assertEqual(self.account.history(), ["Account was created"])

    def test_history_for_int(self):
        int(self.account)
        self.assertEqual(self.account.history(), ["Account was created", "__int__ check -> 0$"])

    def test_history_with_balance_check(self):
        self.account.balance()
        self.assertEqual(self.account.history(), ["Account was created", "Balance check -> 0$"])

    def test_history_for_deposit(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.history(), ["Account was created", "Deposited 1000$"])

    def test_history_for_successful_withdraw(self):
        account = BankAccount("Tester", 100, "$")
        account.withdraw(50)
        self.assertEqual(account.history(), ["Account was created", "50$ was withdrawed"])

    def test_history_for_unsuccessful_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.history(), ["Account was created", "Withdraw for 50$ failed."])

    def test_history_for_transfer_to(self):
        account = BankAccount("Tester", 100, "$")
        result = account.transfer_to(self.account, 50)

        self.assertEqual(self.account.history(), ["Account was created", "Transfer from Tester for 50$"])
        self.assertEqual(account.history(), ["Account was created", "Transfer to Dori for 50$"])
