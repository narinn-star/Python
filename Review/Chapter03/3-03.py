#3-03(a)
year = int(input("year : "))

if year % 4 == 0:
    print("Could be a leap year.")
else:
    print("Definitely not a leap year.")

#3-03(b)
ticket = [1,2,3]
lottery = [1,2,3]

if ticket == lottery:
    print("You won!")
else:
    print("Better luck next time...")