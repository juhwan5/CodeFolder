from operator import mod
import sys
input = sys.stdin.readline

class Multiplication:
    def __init__(self) -> None:
        inp = InputClass()
        multilist = inp.returnli()
        self.numA = multilist[0]
        self.numB = multilist[1]
        self.numC = multilist[2]
        self.anslist = {}
        self.answer = 0
        self.calculating()

    def calculating(self):
        self.answer = self.divideConquer(self.numB)

    def divideConquer(self, depth) -> int:
        if depth in self.anslist:
            return self.anslist[depth]
        
        if depth == 1:
            return self.numA % self.numC
        
        divide_by_2 = depth // 2 
        modA = self.divideConquer(divide_by_2)
        modB = self.divideConquer(depth - divide_by_2)

        calculated_mod = modA * modB % self.numC
        self.anslist[depth] = calculated_mod
        return calculated_mod
        
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

r = Multiplication()
r.printAnswer()