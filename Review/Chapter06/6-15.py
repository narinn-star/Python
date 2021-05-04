phonebook = [{('Anna', 'Karenina'):'(123)456-78-90'},
             {('Yu', 'Tsun'):'(901)234-56-78'},
             {('Hans', 'Castorp'):'(321)908-76-54'},
             {('Anna', 'Miju'):'(345)678-90-12'}]

#print(phonebook[0].keys())
def lookup(phonebook):
    while True:
        first = input("Enter the first name : ")
        last = input("Enter the last name : ")
        
        for i in range(len(phonebook)):
            for j in phonebook[i].keys():
                if j in first:
                    print(phonebook[i])
                elif j in last:
                    print(phonebook[i])
                else:
                    print("ERROR")

lookup(phonebook)