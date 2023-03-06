class WTaste:
    def __init__(self, li) -> None:
        self.WTlist = li   #1차원 배열
        self.answer = 0
        self.calculating()

    def calculating(self):
        anslist = []

        for wt_value in self.WTlist:
            if len(anslist) == 0:
                anslist = [0, wt_value, 0, wt_value]
            else:
                newlist = [max(anslist[0], anslist[2]), max(anslist[0], anslist[2]) + wt_value, max(anslist[1], anslist[3]), anslist[1]+ wt_value]
                anslist = newlist.copy()

        self.answer = max(anslist)

    def printAnswer(self):
        print(self.answer)

class InputClass:
    def __init__(self,num) -> None:
        self.li = []
        self.num = num
        self.mainInput()
        
    def testInput(self):
        pass

    def caseInput(self,i):
        if i == 1:
            self.li = [6,10,13,9,8,1]

    def mainInput(self):
        self.num = int(input())

        for i in range(0,self.num):
            a = int(input())
            self.li.append(a)

    def returnli(self):
        return self.li

inp = InputClass(1)
li = inp.returnli()

r = WTaste(li)
r.printAnswer()