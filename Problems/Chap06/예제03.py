#게시판 페이징하기 *페이징 : 게시판의 페이지 수를 보여주는 것
def getTotalPage(m,n):
    #총 페이지 수 = (총 건수 / 한 페이지당 보여 줄 건수) + 1
    if m % n == 0 :
        return m//n
    else:
        return m // n+1 #소수점 아래 자리를 버리기 위해 // 사용

print(getTotalPage(5, 10))    # 1 출력
print(getTotalPage(15, 10))   # 2 출력
print(getTotalPage(25, 10))   # 3 출력
print(getTotalPage(30, 10))   # 4 출력