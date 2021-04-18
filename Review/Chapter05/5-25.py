def leap(y):
    if y % 4 == 0:
        if y % 100 != 0:
            return True
        else:
            if y % 400 == 0:
                return True
            else:
                return False
    else:
        return False

print(leap(2008))
print(leap(1900))
print(leap(2000))