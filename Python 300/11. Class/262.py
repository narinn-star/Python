#class _ 생성자

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

samsung = Stock("삼성전자", "005930")
print(samsung.name, samsung.code)
