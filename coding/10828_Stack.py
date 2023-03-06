class StackQ:
    def __init__(self) -> None:
        inp = InputClass()
        self.Stacklist = inp.returnli()
        self.answer = []
        self.calculating()

    def calculating(self):
        st = []
        for i in self.Stacklist:
            if i == "top":
                if len(st) == 0:
                    self.answer.append(-1)
                else:
                    self.answer.append(st[len(st)-1])
            elif i == "size":
                self.answer.append(len(st))
            elif i == "pop":
                if len(st) == 0:
                    self.answer.append(-1)
                else:
                    self.answer.append(st.pop())
            elif i == "empty":
                if len(st) == 0:
                    self.answer.append(1)
                else:
                    self.answer.append(0)
            else:
                num = int(i[5:])
                st.append(num)

    def printAnswer(self):
        for i in self.answer:
            print(i)

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
            self.li.append(input())
        
        
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string


r = StackQ()
r.printAnswer()