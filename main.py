from security import Security


class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.security = Security()

    def deposit(self, amount):
        self.security.validate_amount(amount)
        self.balance += amount
        self.security.log_info(
            f"{self.name} deposit {amount}, balance = {self.balance}"
        )

    def withdraw(self, amount):
        self.security.validate_amount(amount)
        self.security.validate_balance(self.balance, amount)
        self.balance -= amount
        self.security.log_info(
            f"{self.name} withdraw {amount}, balance = {self.balance}"
        )
        #member3
