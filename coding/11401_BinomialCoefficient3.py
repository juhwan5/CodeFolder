import sys
input = sys.stdin.readline

class BinomialCoefficient:
    def __init__(self) -> None:
        inp = InputClass()
        BClist = inp.returnli()
        self.N = BClist[0]
        self.K = BClist[1]
        self.NminusK = 0
        self.faclist = [1,1]
        self.p = 1000000007
        self.answer = 0
        self.calculating()

    def calculating(self):
        numA = self.calculFactorial(self.N) % self.p
        self.NminusK = self.calculFactorial(self.K) * self.calculFactorial(self.N - self.K)
        numB = self.divideConquer(self.p-2)
        self.answer = numA * numB % self.p
        
    def calculFactorial(self, num):
        if num < len(self.faclist):
            return self.faclist[num]
        
        while(num >= len(self.faclist)):
            self.faclist.append(len(self.faclist) * self.faclist[len(self.faclist)-1] % self.p)
        return self.faclist[num]
        
    def divideConquer(self, depth) -> int:
        if depth == 1:
            return self.NminusK

        if depth % 2 > 0:
            return self.divideConquer(depth - 1) * self.NminusK % self.p
        
        half = self.divideConquer(depth // 2)
        return half * half % self.p
        
    def printAnswer(self):
        print(self.answer)       

class InputClass:
    def __init__(self) -> None:
        self.string = ""
        self.li = []
        self.num = 0
        self.mainInput(5)
        
    def testInput(self,i):
        pass
            
    def caseInput(self,i):
        if i == 1:
            self.num = 4
            
    def mainInput(self, i):
        self.li = list(map(int, input().rstrip().split()))

    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string

class TestCase:
    def __init__(self, fnc, numlist) -> None:
        self.fnc = fnc
        self.numlist = numlist

r = BinomialCoefficient()
r.printAnswer()