class CStairs:
    def __init__(self, li) -> None:
        self.CSlist = li   #1차원 배열
        self.answer = 0
        self.calculating()

    def calculating(self):
        anslist = []

        for cs_value in self.CSlist:
            if len(anslist) == 0:
                anslist = [0,cs_value, cs_value]
            else:
                newlist = [max(anslist[1], anslist[2]), anslist[0] + cs_value, anslist[1] + cs_value]
                anslist = newlist.copy()

        self.answer = max(anslist[1], anslist[2])

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
            self.li = [10,20,15,25,10,20]

    def mainInput(self):
        self.num = int(input())

        for i in range(0,self.num):
            a = int(input())
            self.li.append(a)

    def returnli(self):
        return self.li

inp = InputClass(1)
li = inp.returnli()

r = CStairs(li)
r.printAnswer()