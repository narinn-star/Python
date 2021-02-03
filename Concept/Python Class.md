## Python Class

1. Class & Object

   + class Cookie:  // 클래스

     ​	pass

     a = Cookie() // 객체

     b = Cookie() // 객체

2. Constructor

   + \_\_init\_\_
     + 메서드 이름을 \_\_init\_\_으로 했기 때문에 생성자로 인식
     + 객체가 생성되는 시점에 자동으로 호출

3. Inheritance

   + How to

     class 클래스 이름(상속할 클래스 이름)

     > 기존 클래스를 변경하지 않고 기능을 추가 및 변경할 때 사용

4. Overriding

   + How to

     class 덮어쓸 클래스 이름(상속할 클래스 이름)

     > 부모 클래스(상속한 클래스)의 메서드 대신 덮어쓴 메서드 호출

5. Class Variable

   + What is..

     class Family :

     ​		lastname = "이"

     > Family 클래스에 선언한 lastname = 변수

   + How to

     print(Family.lastname)

     > 클래스 이름.클래스 변수 

   + Feature

     클래스 변수는 클래스로 만든 모든 객체에 공유

     