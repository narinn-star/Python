#class _ 객체 속성 수정

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
    
    def set_per(self, per):
        self.per = per
    
    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, 수익률):
        self.수익률 = 수익률

samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
samsung.set_per(12.75)
print(samsung.per)