phonebook = {('Anna', 'Karenina'):'(123)456-78-90',
             ('Yu', 'Tsun'):'(901)234-56-78',
             ('Hans', 'Castorp'):'(321)908-76-54'}

def lookup(phonebook):
    while True:
        first = input("Enter the first name : ")
        last = input("Enter the last name : ")
        person = (first, last)
        
        if person in phonebook:
            print(phonebook[person])
        else:
            print("ERROR")

lookup(phonebook)