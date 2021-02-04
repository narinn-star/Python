## Python Module

1. Create a Module

   + def add(a, b):

     ​	return a + b

     def sub(a, b):

     ​	return a - b

2. Load a Module

   + import 모듈파일명

     print(모듈파일명.add(3, 4)) ...

   + from 모듈파일명 import 모듈함수

     add (3, 4)

   + 모든 모듈 다 부르고 싶을 때

     + from 모듈파일명 import add, sub
     + from 모듈파일명 import * 

3. if \_\_name\_\_ == "\_\_main\_\_"