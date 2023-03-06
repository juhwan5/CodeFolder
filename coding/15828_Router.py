from collections import deque
import sys
input = sys.stdin.readline

class Router:
    def __init__(self) -> None:
        inp = InputClass()
        self.num = inp.returnnum()
        self.rtlist = inp.returnli()
        self.answer = []
        self.calculating()

    def calculating(self):
        qu = deque()
        for i in self.rtlist:
            if i == 0:
                qu.popleft()
                continue
            if len(qu) < self.num:
                qu.append(i)
            
        self.answer = qu

                    
    def printAnswer(self):
        if len(self.answer) == 0:
            print("empty")
        else:
            for i in self.answer:
                print(i,end=" ")

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
        self.num = int(input().rstrip())
        while(True):
            tmp = int(input().rstrip())
            if tmp == -1:
                break
            self.li.append(tmp)
            
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string


r = Router()
r.printAnswer()