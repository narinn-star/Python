rphonebook = {'(123)456-78-90':['Anna','Karenina'],
              '(901)234-56-78':['Yu','Tsun'],
              '(321)908-76-54':['Hans','Castorp']}

def rlookup(rphonebook):
    while(True):
        phonenum = input("Enger phone number in the format (xxx)xxx-xx-xx : ")
        if phonenum not in rphonebook:
            print("The number you entered is not in use.")
            continue
        else:
            print([phonenum])

rlookup(rphonebook)