from collections import deque
import sys
input = sys.stdin.readline

class JProblem0:
    def __init__(self) -> None:
        inp = InputClass()
        nk = inp.returnli()
        self.n = nk[0]
        self.k = nk[1]
        self.answer = []
        self.calculating()

    def calculating(self):
        qu = deque(range(1,self.n + 1))
        while(len(qu) != 0):
            for i in range(0,self.k-1):
                qu.append(qu.popleft())
            self.answer.append(qu.popleft())
                    
    def printAnswer(self):
        print("<", end ="")
        for i in range(0, len(self.answer)):
            if i == len(self.answer)-1:
                print(self.answer[i],end=">")
                break
            print(self.answer[i],end=", ")

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
        self.li = list(map(int, input().rstrip().split()))
            
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string


r = JProblem0()
r.printAnswer()