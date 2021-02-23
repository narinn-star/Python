days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def is_on_list(days, day):
    if day in days:
        return True
    else:
        return False

def get_x(days, x):
    return days[x]

def add_x(days, x):
    days.append(x)

def remove_x(days, x):
    days.remove(x)

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)