import sys
input = sys.stdin.readline

class BinomialCoefficient:
    def __init__(self) -> None:
        inp = InputClass()
        self.NM = inp.returnli()
        self.MK = inp.returnli2()
        self.answer = []
        self.calculating()

    def calculating(self):
        numN = len(self.NM)
        numM = len(self.MK)
        numK = len(self.MK[0])
        for n in range(0, numN):
            tmp = []
            for k in range(0, numK):
                NKij = 0
                for m in range(0, numM):
                    NKij += self.NM[n][m] * self.MK[m][k]
                tmp.append(NKij)
            self.answer.append(tmp)
      
    def printAnswer(self):
        for tmp in self.answer:
            for i in range(0,len(tmp)):
                if i == len(tmp)-1:
                    print(tmp[i], end="\n")
                    continue
                print(tmp[i], end=" ")


class InputClass:
    def __init__(self) -> None:
        self.string = ""
        self.li = []
        self.li2 = []
        self.num = 0
        self.mainInput(5)
        
    def testInput(self,i):
        pass
            
    def caseInput(self,i):
        if i == 1:
            self.num = 4
            
    def mainInput(self, i):
        tmp = list(map(int, input().rstrip().split()))
        for k in range(0, tmp[0]):
            self.li.append(list(map(int, input().rstrip().split())))

        tmp = list(map(int, input().rstrip().split()))
        for k in range(0, tmp[0]):
            self.li2.append(list(map(int, input().rstrip().split())))
            

    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnli2(self) -> list:
        return self.li2

    def returnstring(self) -> str:
        return self.string

class TestCase:
    def __init__(self, fnc, numlist) -> None:
        self.fnc = fnc
        self.numlist = numlist

r = BinomialCoefficient()
r.printAnswer()