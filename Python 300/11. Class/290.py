#class _ 부모 클래스 생성자 호출

class parents:
    def __init__(self):
        print("부모 생성")

class children(parents):
    def __init__(self):
        print("자식 생성")
        super().__init__()

me = children()