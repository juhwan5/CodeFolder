import sys
input = sys.stdin.readline

class FindNumber:
    def __init__(self) -> None:
        inp = InputClass()
        self.Nlist = inp.returnli()
        self.Nlist.sort()
        self.Mlist = inp.returnli2()
        self.answer = []
        self.calculating()

    def calculating(self):
        for m in self.Mlist:
            lidx = 0
            ridx = len(self.Nlist)-1
            while(True):
                target = (lidx + ridx) // 2
                if self.Nlist[target] == m:
                    self.answer.append(1)
                    break

                if target == lidx:
                    if self.Nlist[ridx] == m:
                        self.answer.append(1)
                    else:
                        self.answer.append(0)
                    break
                if lidx == ridx:
                    self.answer.append(0)
                    break

                if self.Nlist[target] > m:
                    ridx = target
                else:
                    lidx = target
      
    def printAnswer(self):
        for i in self.answer:
            print(i)


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
        n = int(input())
        self.li = list(map(int, input().rstrip().split()))
        m = int(input())
        self.li2 = list(map(int, input().rstrip().split()))

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

r = FindNumber()
r.printAnswer()