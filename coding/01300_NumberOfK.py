import sys
input = sys.stdin.readline

class NumOfK:
    def __init__(self) -> None:
        inp = InputClass()
        self.n, self.k = inp.returnli()
        self.answer = 0
        self.calculating()

    def calculating(self):
        upper = self.k
        downer = 1
        
        while(True):
            target = (upper + downer) //2
            if target == downer:
                self.answer = upper
                break

            if self.itsOK(target):
                downer = target
            else:
                upper = target

    def itsOK(self, num) -> bool:
        now_seq = 0
        for now_num in range(1, self.n +1):
            now_seq += min(self.n, num//now_num)
            if now_seq >= self.k:
                return False
        return True


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
        for i in range(0,2):
            self.li.append(int(input().rstrip()))
        
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

r = NumOfK()
r.printAnswer()