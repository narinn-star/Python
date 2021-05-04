def encoding(word):
    print("Char  Decimal    Hex    Binary")
    for i in word:
        print(" {:7} {:4d} {:6x} {:9b}".format(i, ord(i),ord(i),ord(i)))

encoding('dad')

#ord() >> 문자열 -> ASCII CODE
#chr() >> CODE -> 문자열