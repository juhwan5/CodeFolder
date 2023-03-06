import sys
input = sys.stdin.readline

class LongestIncreasingSubsequence2:
    def __init__(self) -> None:
        inp = InputClass()
        self.LIS2list = inp.returnli()
        self.answer = 0
        self.calculating()

    def calculating(self):
        anslist = []

        for num in self.LIS2list:
            if len(anslist) == 0:
                anslist.append(num)
                continue

            if num > anslist[len(anslist)-1]:
                anslist.append(num)
                continue

            upidx = len(anslist)-1
            downidx = 0
            while(True):
                targetidx = (upidx + downidx) //2
                if targetidx == downidx:
                    if num <= anslist[downidx]:
                        anslist[downidx] = num
                    else:
                        anslist[upidx] = num
                    break

                if anslist[targetidx] == num:
                    break
                elif anslist[targetidx] < num:
                    downidx = targetidx
                else:
                    upidx = targetidx

        self.answer = len(anslist)
                

    def printAnswer(self):
        print(self.answer)

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
        a = input().rstrip()
        self.li = list(map(int, input().rstrip().split()))
        
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

r = LongestIncreasingSubsequence2()
r.printAnswer()