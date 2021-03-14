#module _ timedelta (5,4,3,2,1일 전 날짜 출력)

import datetime

now = datetime.datetime.now()

for i in range(5, 0, -1):
    delta = datetime.timedelta(days=i)
    date = now - delta
    print(date)