#평균값 구하기 *
f = open('sample.txt')
read = f.readlines()
f.close()


sum = 0
for number in read:
    score = int(number)
    sum += score

avg = sum / len(read)

f = open("result.txt", "w")
f.write(str(avg))
f.close()