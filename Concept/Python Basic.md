## Python Basic

1. 숫자형

   정수형, 실수형, 8진수, 16진수 등

   + Operation
     + 사칙연산
     + **, %, // 연산자

2. 문자열

   + How to

     + "  ", '  ', """ , '''  ☞총 네가지

   + Operation

     + +(연결), *(반복), len()(문자열 길이)

   + Indexing & Slicing

     + 앞 : 0부터 / 뒤 : -1부터 (Indexing)
     + a[0] + a[1] + a[2] + a[3] == a[0:4] (0부터 4개) 

   + Formatting

     + 숫자, 문자열, 변수 혹은 2개 이상의 값을 문자열 안에 대입

       Ex) >>> number = 3

       ​	  >>>"I eat %d apples." % number

       ​	  'I eat 3 apples.'

     + Formatting by format function

       Ex) >>> "I eat {0} apples".format(3)

       ​	  'I eat 3 apples'

       ​	※ 문자열 앞에 f 접두사 붙이면 포매팅 기능 사용 가능

   + Functions

     + .count (문자 개수) / .find (위치 1) / .index (위치 2) / .join (문자열 삽입) / .upper(소문자->대문자) / .lower (대문자->소문자) / .lstrip(左공백 지우기) / .rstrip(右공백 지우기) / .strip (양쪽 공백 지우기) / .replace (문자열 바꾸기) / .split (문자열 나누기)

3. 리스트

   + How to 

     + \>\>\> odd = [1, 3, 5, 7, 9]
     + 어떠한 자료형도 포함 가능

   + Indexing & Slicing 

     + 문자열에서 사용한 것과 매우 유사
     + 중첩, 삼중 리스트 가능

   + Operation

     + +(연결), *(반복), len()(길이)

       EX) \>>> a = [1, 2, 3]

       ​	   \>>> a[2] + "hi"

       ​	※ 정수와 문자열은 더할 수 없기 때문에 str함수로 "숫자 3"을 "문자 3"으로 바꿈

       ​	   \>>> str(a[2]) + "hi"

   + Modify & Delete

     + 삭제 ☞ del 함수 사용 (del 객체명)

   + Functions

     + .append (요소 추가) / .sort (정렬) / .reverse (뒤집기) / .index (위치) / .insert (삽입) / .remove (제거) / .pop (꺼내기) / .count (요소 개수) / .extend (확장)

4. 튜플

   + How to

     + \>>> t1 = (1, )

     + 1개의 요소만 가질때는 요소 뒤 콤마 필수

     + 괄호 필수 X

       ※ 리스트와 달리 항목 값 변화 X

   + Modify & Delete 

     + 수정 & 삭제 ☞ Error Message

   + Indexing & Slicing

     + 문자열, 리스트와 마찬가지

   + Operation

     + +(연결), *(반복), len()(길이)

5. 딕셔너리

   + How to

     + {Key1:Value1, Key2:Value2, Key3:Value3, ...}

   + Add & Delete

     + \>>> a = {1: 'a'}

       \>>> a[2] = 'b'

       \>>> a

       {1: 'a', 2: 'b'}

       > 딕셔너리 a에 Key와 Value가 각각 2와 'b'인 딕셔너리 쌍 추가

     + \>>> del a[1]

       \>>> a

       {2 : 'b'}

       > 딕셔너리 a에 지정한 Key에 해당하는 {key : value} 쌍 삭제

   + Caution

     + 동일한 Key 존재 X

     + Key에 리스트 X

       단, Value에는 어떤 값이든 상관 없음

   + Functions

     + .keys (Key 리스트) / .values (Value 리스트) / .items (Key, Value 쌍) / .clear (모두 지우기) / .get (Key로 Value 얻기) / .in (Key 존재여부)

6. 집합

   + How to

     + \>>> s1 = set([1,2,3])

       \>>> s1

       {1, 2, 3}

     > ※ 중복 허용 X , 순서 X

   + Type

     ​	\>>> s1 = set ([1, 2, 3, 4, 5, 6])

     ​	\>>> s2 = set ([4, 5, 6, 7, 8, 9])

     + 교집합 (Intersection)

       1) s1 & s2

       2) s1.intersection(s2)

       => {4, 5, 6}

     + 합집합 (Union)

       1) s1 | s2

       2) s1.union(s2)

       => {1, 2, 3, 4, 5, 6, 7, 8, 9}

     + 차집합 (Difference)

       1) s1 - s2

       2) s1.difference(s2)

       => {8, 9, 7}

   + Functions

     + .add (값 1개 추가) / .update (값 여러개 추가) / .remove (특정 값 제거)

7. 불

   + How to

     + True / False 

       > true / false ☞ X

   + T or F  in Data Type

     + "data" : True / "" : False / [1, 2, 3] : True / [], (), & {} : False / 

       1 : True / 0 : False / None : False

8. 변수

   + How to

     + assignment sign (=)

       > 스스로 판단 후 자료형 지정

   + Copy (List)
     + Using : (colon)
     + Using copy module