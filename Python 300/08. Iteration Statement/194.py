#for문 _ 이차원 리스트 -> 이차원 리스트

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

a = 1.00014
result = []

for i in data:
    result2 = []
    for j in i:
        total = j * a
        result2.append(total)
    result.append(result2)

print(result)
