class SSequence:
    def __init__(self) -> None:
        inp = InputClass()
        self.SSlist = inp.returnli()
        self.num = inp.returnnum()
        self.answer = []
        self.calculating()

    def calculating(self):
        st =[]
        idx = 0
        i = 1
        while idx < self.num:
            val = self.SSlist[idx]
            if i <= val:
                st.append(i)
                i += 1
                self.answer.append("+")
            else:
                popop = st.pop()
                if popop != val:
                    self.answer = ["NO"]
                    break
                else:
                    self.answer.append("-")
                    idx += 1

            

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
            self.li.append(int(input()))
        
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string


r = SSequence()
r.printAnswer()