#class _ 객체 생성

class Stock:
    def __init__(self, name, code, per, pbr, 수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.수익률 = 수익률

    def set_name(self, name):
        self.name = name
    
    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
print(samsung.name, samsung.code, samsung.per, samsung.pbr, samsung.수익률)