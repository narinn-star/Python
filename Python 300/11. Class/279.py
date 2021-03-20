#class _ 객체 순회

import random

class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        
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

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = (self.balance * 1.01)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def display_info(self):
        print("은행 이름 : " , self.bank)
        print("예금주 : ", self.name)
        print("계좌번호 : ", self.account_number)
        res = format(self.balance, ',d') #format 함수 사용 => format(값, "형식규칙") OR "{형식규칙}".format(값) ** ',d' : int형, ',' : int, float형
        print("잔고 : ", res, "\b원")

data = []

kim=Account("김민서", 10000)
lee=Account("이나린", 200000)
woo=Account("이승우", 3000000)

data.append(kim)
data.append(lee)
data.append(woo)

#print(data)

for i in data:
    if i.balance >= 1000000:
        i.display_info()