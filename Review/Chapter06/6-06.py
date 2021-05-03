phonebook1 = {'123-45-67', '234-56-78', '345-67-89'}
phonebook2 = set()
phonebook3 = {'345-67-89', '456-78-90'}
phonebook4 = {'234-56-78', '456-78-90'}
phonebooks = [phonebook1, phonebook2, phonebook3,phonebook4]

def sync(phonebooks):
    res = set()
    for number in phonebooks:
        res = res | number
    
    print(res)

sync(phonebooks)