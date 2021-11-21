class BankAccount:
    def __init__(self, name, start_balance, currency):
        if start_balance < 0:
            raise ValueError("Start balance must be positive")

        self.__balance = start_balance
        self.__name = str(name)
        self.__currency = str(currency)
        self.__history = []

        self.__make_history("Account was created")

    def __int__(self):
        self.__make_history("__int__ check -> {}$".format(self.__balance))
        return self.__balance

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.__name, self.__balance, self.__currency)

    def __make_history(self, event):
        self.__history.append(event)

    def balance(self):
        self.__make_history("Balance check -> {}{}".format(self.__balance, self.__currency))
        return self.__balance

    def holder(self):
        return self.__name

    def currency(self):
        return self.__currency

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative amount.")
        self.__balance += amount
        self.__make_history("Deposited {}$".format(amount))

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            self.__make_history("Withdraw for {}$ failed.".format(amount))
            return False
        self.__balance -= amount
        self.__make_history("{}$ was withdrawed".format(amount))
        return True

    def transfer_to(self, account, amount):
        if self.currency() == account.currency():
            self.withdraw(amount)
            account.deposit(amount)
            l1 = len(self.history())
            l2 = len(account.history())
            del self.history()[l1 - 1]
            del account.history()[l2 - 1]
            self.__make_history("Transfer to {} for {}{}".format(account.__name, amount, self.__currency))
            account.__make_history("Transfer from {} for {}{}".format(self.__name, amount, self.__currency))
            return True

    def history(self):
        return self.__history
