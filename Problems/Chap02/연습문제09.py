a = dict()
print(a)

#다음 중 오류가 발생하는 경우?
#1. a['name'] = 'python'
#2. a[('a',)] = 'python' 
#3. a[[1]] = 'python' => 정답 : 리스트는 Key가 될 수 없다
#4. a[250] = 'python'

# +) Key로는 변하는 값을 사용할 수 없다. 
# 문자열, 튜플, 숫자는 변하지 않는 값