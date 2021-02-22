days = ["Mon", "Tue", "Wed", "Thur", "Fri"]

print(days, type(days))
print("Mon" in days) #Mon이 days 안에 있는가 ? => True/False
print(days[2])
print(len(days))
days.append("Sat") #Mutable
days.reverse()
print(days)
