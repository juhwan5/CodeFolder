class GStation:
    def __init__(self) -> None:
        inp = InputClass()
        a = inp.returnli()
        self.Loadlist = a[0]
        self.GSlist = a[1]
        self.answer = 0
        self.calculating()

    def calculating(self):
        gas_cost = self.GSlist[0]
        nowpoint = 0
        for i in range(0, len(self.Loadlist)):
            if self.GSlist[i] < gas_cost:
                gas_cost = self.GSlist[i]
            self.answer += gas_cost * self.Loadlist[i]

    def printAnswer(self):
        print(self.answer)

class InputClass:
    def __init__(self) -> None:
        self.string = ""
        self.li = []
        self.num = 0
        self.mainInput(2)
        
    def testInput(self,i):
        pass

    def caseInput(self,i):
        if i == 1:
            self.num = 4
            self.li = [[2,3,1], [5,2,4,1]]
        if i == 2:
            self.num = 4
            self.li = [[3,3,4],[1,1,1,1]]

    def mainInput(self, i):
        a = int(input())
        b = list(map(int,(input().split())))
        c = list(map(int,(input().split())))
        self.li.append(b)
        self.li.append(c)
        
        
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string


r = GStation()
r.printAnswer()