class A:
    def __init__(self):
        self.a = 10


    def _init_fun(self):
        self.b = 20
    
    def prnt(self):
        self._init_fun()
        print(self.a, self.b)

a = A()
a.prnt()