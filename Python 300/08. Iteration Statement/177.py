#for문 _ 인덱스 이용3

my_list = ["가", "나", "다", "라"]

for i in range(len(my_list) - 1, 0, -1):
    print(my_list[i], my_list[i-1])