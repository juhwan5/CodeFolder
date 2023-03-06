from collections import deque

class Card2:
    def __init__(self) -> None:
        inp = InputClass()
        self.num = inp.returnnum()
        self.answer = 1
        self.calculating()

    def calculating(self):
        qu = deque(range(1,self.num+1))
        while(len(qu) > 1):
            qu.popleft()
            self.answer = qu.popleft()
            qu.append(self.answer)
                    
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
            
    def mainInput(self, i):
        self.num = int(input())
            
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string


r = Card2()
r.printAnswer()