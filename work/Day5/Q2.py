class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Saji", 1000)

acc.deposit(500)
print("Balance after deposit:", acc.get_balance())

acc.withdraw(300)
print("Balance after withdraw:", acc.get_balance())
   