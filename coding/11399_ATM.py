class ATM:
    def __init__(self) -> None:
        inp = InputClass()
        self.ATMlist = inp.returnli()
        self.ATMlist.sort()
        self.answer = 0
        self.calculating()

    def calculating(self):
        nowtime = 0
        for i in self.ATMlist:
            nowtime += i
            self.answer += nowtime

    def printAnswer(self):
        print(self.answer)

class InputClass:
    def __init__(self) -> None:
        self.string = ""
        self.li = []
        self.num = 0
        self.mainInput(1)
        
    def testInput(self,i):
        pass

    def caseInput(self,i):
        if i == 1:
            self.num = 3
            self.li = [1,2,3,1,2]
        if i == 2:
            self.num = 10
            self.li = [5,8,2,5,9,3,2,7,9,6]


    def mainInput(self, i):
        self.num = int(input())
        self.li = list(map(int, input().split()))
        

    def returnnum(self):
        return self.num

    def returnli(self):
        return self.li

    def returnstring(self):
        return self.string


r = ATM()
r.printAnswer()