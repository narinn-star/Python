#class _ 클래스 메서드

import random

class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3) # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count) #Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

kim = Account("김민서", 100)
print(kim.name, kim.balance, kim.bank, kim.account_number)
kim.deposit(500)
print(kim.balance)
kim.withdraw(400)
print(kim.balance)
lee = Account("이나린", 200)
print(lee.name, lee.balance, lee.bank, lee.account_number)
lee.deposit(1000)
print(lee.balance)
lee.withdraw(200)
print(lee.balance)
kim.get_account_num()