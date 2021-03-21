#class _ 메서드 오버라이딩

class parents:
    def call(self):
        print("부모 호출")
    
class children(parents):
    def call(self):
        print("자식 호출")

me = children()
me.call()