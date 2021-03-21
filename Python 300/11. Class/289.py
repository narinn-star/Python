#class _ 생성자

class parents:
    def __init__(self):
        print("부모 생성")

class children(parents):
    def __init__(self):
        print("자식 생성")

me = children()