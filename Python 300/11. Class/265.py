#class _ 메서드

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name
    
    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

samsung = Stock("삼성전자", "005930")
print(samsung.name, samsung.code)
print(samsung.get_name)
print(samsung.get_code)