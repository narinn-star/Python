#3-02(a)
age = int(input("나이 입력 : "))

if age >= 62:
    print("You can get your pension benefits")
else:
    print("ERR")

#3-02(b)
name = input("이름 입력 : ")

namelst = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']

if name in namelst:
    print("One of the top 5 baseball players, ever!")
else:
    print("ERR")

#3-02(c)
hits = int(input("hits : "))
shield = int(input("shield : "))

if hits > 10 and shield == 0:
    print("You are dead...")
else:
    print("LIVE")

#3-02(d)
north = True 
south = False
east = False
west = True

if north == True or south == True or east == True or west == True:
    print("I can escape.")
else:
    print("ERR")