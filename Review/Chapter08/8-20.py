class BankAccount:
    def __init__(self, money):
        self.money = money

    def withdraw(self, money):
        self.money -= money
    
    def deposit(self, money):
        self.money += money
    
    def balance(self):
       return self.money

x = BankAccount(700)
print("{:.2f}".format(x.balance()))

x.withdraw(70)
print("{:.2f}".format(x.balance()))

x.deposit(7)
print("{:.2f}".format(x.balance()))