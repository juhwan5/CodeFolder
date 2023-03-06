from collections import deque
import sys
input = sys.stdin.readline

class MatrixMultiplicationOrder:
    def __init__(self) -> None:
        inp = InputClass()
        self.stlist = inp.returnli()
        self.edlist = inp.returnli2()
        self.answer = 0
        self.calculating()

    def calculating(self):
        dp = [[0] for _ in range(len(self.stlist))]
        for loop in range(1, len(self.stlist)):
            for i in range(0, len(self.stlist)):
                j = i+loop
                if j >= len(self.stlist):
                    break
                valist = []
                for k in range(i, j):
                    mul = self.stlist[i] * self.edlist[k] * self.edlist[j]
                    val = dp[i][k-i] + dp[k+1][j-k-1] + mul
                    valist.append(val)
                
                dp[i].append(min(valist))
        
        self.answer = dp[0][len(self.stlist)-1]

                    
    def printAnswer(self):
        print(self.answer)

class InputClass:
    def __init__(self) -> None:
        self.string = ""
        self.li = []
        self.li2 = []
        self.num = 0
        self.mainInput(2)
        
    def testInput(self,i):
        pass

    def caseInput(self,i):
        if i == 1:
            self.num = 4
            
    def mainInput(self, i):
        a = int(input().rstrip())
        for i in range(0,a):
            st, ed = list(map(int, input().rstrip().split()))
            self.li.append(st)
            self.li2.append(ed)

            
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnli2(self) -> list:
        return self.li2
    
    def returnstring(self) -> str:
        return self.string


r = MatrixMultiplicationOrder()
r.printAnswer()