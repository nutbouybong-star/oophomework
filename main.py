class accout:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposite(self, amount):
        if amount <= 0:
            print("deposite amount")
            return
        self._balance += amount
        print(f"deposite[{amount}]. current balance: [{self.balance}]")
    def withdraw(self, amount):
        if amount <= 0:
            print("withdraw amount")
            return 
        if amount > self.balance:
            print("withdraw failed.")
            return 
        self.balance -= amount
        print(f"withdraw[{amount}]. current balance: {self.balance}")
        #member1
        