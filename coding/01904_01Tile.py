class AlgorythmFibo1:
    def __init__(self, num) -> None:
        self.num = num
        self.a = 0
        self.b = 1
        self.fib2 = self.doFib(self.num)

    def printA(self):
        print(self.fib2)

    def doFib(self, num):
        for i in range(0,num):
            res = self.a + self.b
            self.a = self.b % 15746
            self.b = res % 15746
        return self.b

a = int(input())
b = AlgorythmFibo1(a)
b.printA()
