class myStr(str):

    def __init__(self, string):
        self.string = string

    def __add__(self, other):
        return len(self) + len(other)

    def __mul__(self, other):
        return len(self) * len(other)

x = myStr('hello')
print(x + 'universe')
print(x * 'universe')