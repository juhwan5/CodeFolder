import sys
input = sys.stdin.readline

class NumberCard2:
    def __init__(self) -> None:
        inp = InputClass()
        self.Nlist = inp.returnli()
        self.Nlist.sort()
        self.Mlist = inp.returnli2()
        self.answer = []
        self.calculating()

    def calculating(self):
        ans_dict = {}
        for i in self.Nlist:
            if i in ans_dict:
                ans_dict[i] += 1
            else:
                ans_dict[i] = 1
        dictkeys = list(ans_dict.keys())

        for m in self.Mlist:
            lidx = 0
            ridx = len(dictkeys)-1
            while(True):
                target = (lidx + ridx) // 2
                if dictkeys[target] == m:
                    self.answer.append(ans_dict[m])
                    break
                if target == lidx:
                    if dictkeys[ridx] == m:
                        self.answer.append(ans_dict[m])
                    else:
                        self.answer.append(0)
                    break
                if lidx == ridx:
                    self.answer.append(0)
                    break

                if dictkeys[target] > m:
                    ridx = target
                else:
                    lidx = target
      
    def printAnswer(self):
        for i in self.answer:
            print(i, end=" ")


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

r = NumberCard2()
r.printAnswer()