## Python Module

1. Create a Module

   + def add(a, b):

     ​	return a + b

     def sub(a, b):

     ​	return a - b

2. Loading a Module

   + import 모듈파일명

     print(모듈파일명.add(3, 4)) ...

   + from 모듈파일명 import 모듈함수

     add (3, 4)

   + 모든 모듈 다 부르고 싶을 때

     + from 모듈파일명 import add, sub
     + from 모듈파일명 import * 

3. if \_\_name\_\_ == "\_\_main\_\_": 

   + 함수만 사용하려 할 때

     \_\_main\_\_은 모듈파일

     다른 곳에서 모듈파일을 실행하면 \_\_name\_\_ != \_\_main\_\_ 이기 때문에 오류

4. Modules including Class & Variable

   + 클래스

     a = 모듈파일명.클래스명()

   + 변수

     print(모듈파일명.변수)

5. Loading Module from Other File

   + 파일들이 동일 디렉터리에 있어야 함

