phonebook = {('Anna', 'Karenina'):'(123)456-78-90',
             ('Yu', 'Tsun'):'(901)234-56-78',
             ('Hans', 'Castorp'):'(321)908-76-54'}

def lookup(phonebook):
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")

    name = (first, last)
    if name in phonebook:
        print(phonebook[name])

lookup(phonebook)