from collections import deque
import sys
input = sys.stdin.readline

class SQueue:
    def __init__(self) -> None:
        inp = InputClass()
        self.num = inp.returnnum()
        self.SQlist = inp.returnli()
        self.answer = 0
        self.calculating()

    def calculating(self):
        qu = deque(list(range(1, self.num +1)))
        for target in self.SQlist:
            tasking = 0
            while(True):
                popnum = qu.popleft()
                if popnum == target:
                    self.answer += min(tasking, len(qu) + 1 - tasking)
                    break
                qu.append(popnum)
                tasking += 1

                  
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
        self.num, tmp = map(int, input().rstrip().split())
        self.li = list(map(int, input().rstrip().split()))
        
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string

class TestCase:
    def __init__(self, n, m, importance) -> None:
        self.n = n
        self.m = m
        self.importance = importance


r = SQueue()
r.printAnswer()