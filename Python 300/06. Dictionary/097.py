#딕셔너리 메서드 _ values()

icecream = {"탱크보이":1200, "폴라포":1200, "빵빠레":1800, "월드콘":1500, "메로나":1000}

result = 0
for i in icecream.values():
    result += i
print("방법 1 : ", result)

print("방법 2 : ", sum(icecream.values()))