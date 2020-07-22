import pytz
import datetime


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self.name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append(
                (Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("You don't have that much to withdraw. ")
        self.show_balance()

    def show_balance(self):
        print("Balance is {} ".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})"
                  .format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    hayden = Account("Hayden", 0)
    hayden.show_balance()

    hayden.deposit(1000)
    hayden.withdraw(500)
    hayden.withdraw(4000)
    hayden.show_transactions()

    steve = Account("steve", 1000)
    steve.deposit(100)
    steve.withdraw(100)
    steve.show_transactions()