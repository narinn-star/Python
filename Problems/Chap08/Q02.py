#딕셔너리 값 추출하기
try:
    a = {'A':90, 'B':80}
    print(a['C'])
except KeyError:
    print(70)