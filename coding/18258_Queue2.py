import sys
input = sys.stdin.readline
from collections import deque
class Queue2:
    def __init__(self) -> None:
        inp = InputClass()
        self.Q2list = inp.returnli()
        self.answer = []
        self.calculating()

    def calculating(self):
        qu = deque()
        for exe in self.Q2list:
            if exe == "size":
                self.answer.append(len(qu))
            elif exe == "empty":
                if len(qu) == 0:
                    self.answer.append(1)
                else:
                    self.answer.append(0)
            elif exe[0:4] == "push":
                num = int(exe[5:])
                qu.append(num)
            else:
                if len(qu) > 0:
                    if exe == "pop":
                        self.answer.append(qu.popleft())
                    elif exe == "front":
                        self.answer.append(qu[0])
                    elif exe == "back":
                        self.answer.append(qu[len(qu)-1])
                else:
                    self.answer.append(-1)
                    
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
            self.li.append(input().rstrip())
            
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string


r = Queue2()
r.printAnswer()