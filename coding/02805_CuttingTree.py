import sys
input = sys.stdin.readline

class CTree:
    def __init__(self) -> None:
        inp = InputClass()
        self.n = inp.returnnum()
        self.CTlist = inp.returnli()
        self.CTlist.sort(reverse = True)
        self.answer = 0
        self.calculating()

    def calculating(self):
        upper = sum(self.CTlist) // len(self.CTlist)
        downer = 0
        while(True):
            if self.itsOK(upper):
                upper *= 2
            else:
                break

        while(True):
            target = (upper + downer) //2
            if target == downer:
                self.answer = downer
                break

            if self.itsOK(target):
                downer = target
            else:
                upper = target


    def itsOK(self, num) -> bool:
        woods = 0
        for i in self.CTlist:
            if i <= num:
                return False

            woods += i - num
            if woods >= self.n:
                return True
        
        return False


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
        a, self.num = list(map(int, input().rstrip().split()))
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

r = CTree()
r.printAnswer()