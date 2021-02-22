#딕셔너리 _ 별 표현식 (star expression)

#a, b, *c = (0,1,2,3,4,5)
#print(a) => 0
#print(b) => 1
#print(c) => [2, 3, 4, 5]

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,a,b = scores
print(valid_score)