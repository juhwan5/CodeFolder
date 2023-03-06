from collections import deque
import sys
input = sys.stdin.readline

class PQueue:
    def __init__(self) -> None:
        inp = InputClass()
        self.PQlist = inp.returnli()
        self.answer = []
        self.calculating()

    def calculating(self):
        for tcase in self.PQlist:
            qu = deque(tcase.importance)
            li = []
            nowprint = tcase.importance.copy()
            nowprint.sort(reverse = True)
            qu[tcase.m] *= -1
            ans = 0
            while(True):
                tmp = qu.popleft()
                if abs(tmp) != nowprint[ans]:
                    qu.append(tmp)
                    continue
                ans += 1
                if tmp < 0:
                    self.answer.append(ans)
                    break

                  
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
            
    def mainInput(self, i):
        cnt = int(input().rstrip())
        for i in range(0, cnt):
            a = list(map(int, input().rstrip().split()))
            b = list(map(int, input().rstrip().split()))
            self.li.append(TestCase(a[0], a[1], b))

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


r = PQueue()
r.printAnswer()