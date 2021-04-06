def noVowel(s):
    count = 0
    for i in s:
        if i == 'a' or i == 'e' or i =='i' or i == 'o' or i == 'u':
            count = count + 1
    if count > 0:
        print(False)
    else:
        print(True)

s = input("단어 입력 >> ")
noVowel(s)