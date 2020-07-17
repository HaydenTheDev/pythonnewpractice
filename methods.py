class Account:
    """Simple account class with balance"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("You don't have that much to withdraw. ")
        self.show_balance()

    def show_balance(self):
        print("Balance is {} ".format(self.balance))


if __name__ == "__main__":
    hayden = Account("Hayden", 0)
    hayden.show_balance()

    hayden.deposit(1000)
    hayden.withdraw(500)
    hayden.withdraw(4000)