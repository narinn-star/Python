#class _ 여러 객체 생성

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
hyundai = Stock("현대차", "005380", 8.70, 0.35, 4.27)
lg = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

result = []

result.append(samsung)
result.append(hyundai)
result.append(lg)

for i in result:
    print(i.code, i.per)