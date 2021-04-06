def allEven(nums):
    count = 0
    for i in nums:
        if i % 2 != 0:
            count = count + 1
    if count > 0:
        print(False)
    else:
        print(True)

allEven([8, 0, -2, 4, -6, 10])
allEven([8, 0, -1, 4, -6, 10])