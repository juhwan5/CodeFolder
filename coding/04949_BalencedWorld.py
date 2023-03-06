class BWorld:
    def __init__(self) -> None:
        inp = InputClass()
        self.BWlist = inp.returnli()
        self.answer = []
        self.calculating()

    def calculating(self):
        for i in self.BWlist:
            st = []
            opener = ["(", "["]
            closer = [")", "]"]
            ans = "yes"
            for j in i:
                if j in opener:
                    st.append(j)
                    continue

                if j in closer:
                    if len(st) > 0:
                        idx = closer.index(j)
                        if st.pop() != opener[idx]:
                            ans = "no"
                            break
                    else:
                        ans = "no"
                        break

            if len(st) != 0:
                ans = "no"
            
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
        st = ""
        while(st != "."):
            st = input()
            self.li.append(st)
        
        self.li.pop()
        
        
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string


r = BWorld()
r.printAnswer()