first = input("Enter first word : ")
second = input("Enter second word : ")
third = input("Enter third word : ")

if first[0] < second[0] and second[0] < third[0]:
    print(True)
else:
    print(False)