#for문 _ 이차원 리스트 출력

apart = [ [101, 102], [201, 202], [301, 302] ]

for i in apart[::-1]:
    for j in i[::-1]:
        print(j, "호")