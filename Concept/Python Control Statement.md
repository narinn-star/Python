## Python Control Statement

1. if 조건문 (Conditional Statements)

   + Structure

     if 조건문:

     (들여쓰기)수행할 문장1

     else:

     (들여쓰기) 수행할 문장A

   + Indentation & Colon

     + 들여쓰기 필수

     + 조건문 뒤에 콜론 필수

   + elif

     + else if와 같은 역할

   + Conditional Expression

     + if score >= 60 : message = "success"

       else : message = "failure"

       위 코드를 조건부 표현식을 사용

     + message = "success" if score >= 60 else "failure"

     + "조건문이 참인 경우" if "조건문" else "조건문이 거짓인 경우"

2. while 반복문(Iteration)

   + Structure

     while 조건문:

     (들여쓰기) 수행할 문장

   + break, continue

     + break : 강제로 빠져나가기
     + continue : 맨 처음(조건문)으로 돌아가기

   + Infinite Loop

     + while True:

       ​	수행할 문장1 ...

       > while문의 조건문이 True이므로 항상 참 (무한 루프)

3. for 반복문(Iteration)

   + Structure

     for 변수 in 리스트/튜플/문자열 :

     (들여쓰기) 수행할 문장

   + continue

     while문과 동일함 (for문의 처음으로 돌아가기)

   + Function_range

     + \>>>a = range(10)

       \>>>a 

       range(0,10)

       > range(10)은 0부터 10 미만의 숫자를 포함하는 range 객체 만들기

   + List Comprehension

     + 리스트 안에 for문을 포함

       EX)

       \>>>a = [1,2,3,4]

       \>>>result = [num * 3 for num in a]

       \>>>print(result)

       [3, 6, 9, 12]