class ZEROQ:
    def __init__(self) -> None:
        inp = InputClass()
        self.Zerolist = inp.returnli()
        self.answer = 0
        self.calculating()

    def calculating(self):
        st = []
        for i in self.Zerolist:
            if i == 0:
                st.pop()
            else:
                st.append(i)
        self.answer = sum(st)
        

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
        self.num = int(input())
        for i in range(0, self.num):
            self.li.append(int(input()))
        
        
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string


r = ZEROQ()
r.printAnswer()