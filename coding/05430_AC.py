from collections import deque
import random
import sys
input = sys.stdin.readline

class AC:
    def __init__(self) -> None:
        inp = InputClass()
        self.num = inp.returnnum()
        self.AClist = inp.returnli()
        self.answer = []
        self.calculating()

    def calculating(self):
        for tcase in self.AClist:
            isleft : bool = True
            isntErrored : bool = True
            qu = deque(tcase.numlist)
            for i in tcase.fnc:
                if i == "R":
                    isleft = not(isleft)
                    continue
                if len(qu) == 0:
                    self.answer.append("error")
                    isntErrored = False
                    break
                if isleft:
                    qu.popleft()
                else:
                    qu.pop()
            
            if isntErrored:
                if not(isleft):
                    qu.reverse()
                string = "["
                for i in range(0,len(qu)):
                    if i == len(qu) -1:
                        string = string + str(qu[i])
                        break
                    string = string + str(qu[i]) + ","
                string += "]"
                self.answer.append(string)
                    

    def printAnswer(self):
        for i in self.answer:
            print(i)

class InputClass:
    def __init__(self) -> None:
        self.string = ""
        self.li = []
        self.num = 0
        self.mainInput(5)
        
    def testInput(self,i):
        for x in range(0,i):
            fnc = ""
            cnt = random.randint(2,10)
            for y in range(0,cnt):
                rd = random.randint(0,1)
                if rd == 0:
                    fnc += "R"
                else:
                    fnc += "D"

            cnt = random.randint(0,10)
            tmp = []
            for z in range(0,cnt):
                rdint = random.randint(1,101)
                tmp.append(rdint)
            self.li.append(TestCase(fnc, tmp))
            


    def caseInput(self,i):
        if i == 1:
            self.num = 4
            
    def mainInput(self, i):
        self.num = int(input().rstrip())
        for i in range(0,self.num):
            fnc = input().rstrip()

            tmp = input().rstrip()
            numinput = input().rstrip()
            if len(numinput) <= 2:
                numlist = []
            else:
                numlist = list(map(int, numinput[1:len(numinput)-1].split(",")))
            
            self.li.append(TestCase(fnc, numlist))

    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string

class TestCase:
    def __init__(self, fnc, numlist) -> None:
        self.fnc = fnc
        self.numlist = numlist

r = AC()
r.printAnswer()