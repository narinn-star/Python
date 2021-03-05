#for문 _ 이차원 리스트 출력

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

sum = 0

for i in ohlc[1:]:
    sum += (i[3] - i[0])

print(sum)