rphonebook = {'(123)456-78-90':['Anna','Karenina'],
              '(901)234-56-78':['Yu', 'Tsun'],
              '(321)908-76-54':['Hans', 'Castorp']}

def rlookup(rphonebook):
    while True:
        try:
            find = input("Enter phone number in the format (xxx)xxx-xx-xx : ")
            print(rphonebook[find])
        except(KeyError):
            print("The number you entered is not in use")
            continue

rlookup(rphonebook)
