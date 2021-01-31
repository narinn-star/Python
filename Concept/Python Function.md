## Python Function

+ Structure

  + def 함수명 (매개변수) : 

    ​	<수행할 문장>

    ​	...

    > def는 예약어

+ Parameter & Arguments

  + 매개변수 : 함수에 입력으로 전달된 값을 받는 변수
  + 인수 : 함수를 호출할 때 전달하는 입력값

+ Type of Function

  + 일반 함수

    > 결과값을 받을 변수 = 함수이름(입력인수1,입력인수2, ...)

  + 입력값이 없는 함수 (매개변수 X)

    > 결과값을 받을 변수 = 함수이름()

  + 결과값이 없는 함수 (return 명령어 X)

    > 함수이름(입력인수1, 입력인수2, ...)

  + 입력값과 결과값이 없는 함수 (매개변수 X, return 명령어 X)

    > 함수이름()
  
+ Many Inputs(Parameters)

  + EX)

    ​	def add_many(*args)

    > 매개변수 이름 앞에 '*' (=> 입력값을 모아 튜플로)
    >
    > 매개변수 이름 앞에 '**' (=> 입력값을 딕셔너리로)

+ Modify Variable outside Function

  + return 사용
    + return 해주는 값을 함수의 결과값으로 바꾸기 등
  + global 명령어 사용
    + global a ☞ 함수 내에서 함수 밖의 a 변수를 직접 사용
    + 사용을 권장하지는 않음

+ lambda

  > def를 사용할 수 없는 곳 or def가 필요하지 않는 경우

  + lambda 매개변수 1, 2, ... : 표현식

    + EX)

      ​	\>>> add = lamda a, b : a+b

      ​	\>>> result = add (3, 4)

      ​	\>>> print(result)

      ​	7

      > lambda 예약어로 만든 함수는 return 없이도 결과값 O