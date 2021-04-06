def average(a, b):
    'a와 b의 평균을 반환함'
    int(a)
    int(b)
    print((a + b) / 2)

def negatives(nums):
    '음수를 하나씩 반환'
    for i in nums:
        if i <0:
            print(i)

help(average)
help(negatives)