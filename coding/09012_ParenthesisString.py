class PString:
    def __init__(self) -> None:
        inp = InputClass()
        self.PSlist = inp.returnli()
        self.answer = []
        self.calculating()

    def calculating(self):
        for i in self.PSlist:
            st = []
            ans = "YES"
            for j in i:
                if j == "(":
                    st.append(0)
                else:
                    if len(st) > 0:
                        st.pop()
                    else:
                        ans = "NO"
                        break
            
            if len(st) != 0:
                ans = "NO"
            
            self.answer.append(ans)

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


r = PString()
r.printAnswer()