import sys
input = sys.stdin.readline

class PNumber:
    def __init__(self) -> None:
        inp = InputClass()
        self.num = inp.returnnum()
        self.PNlist = inp.returnli()
        self.minus = 0
        self.zero = 0
        self.plus = 0
        self.calculating()

    def calculating(self):
        tmp = self.divideConquer(0,0,len(self.PNlist[0]))
        if tmp == -1:
            self.minus += 1
        elif tmp == 0:
            self.zero += 1
        elif tmp == 1:
            self.plus += 1

    def divideConquer(self, col_start, row_start, given_length) -> int:
        if given_length == 1:
            return self.PNlist[col_start][row_start]
        
        now_length : int = given_length // 3
        anslist = []
        for i in range(0,9):
            col = i //3
            row = i % 3
            partition = self.divideConquer(col_start + (col * now_length), row_start + (row *now_length), now_length)
            anslist.append(partition)
        
        anslist.sort()
        if anslist[0] == anslist[len(anslist)-1] and anslist[0] != -2:
            return anslist[0]
        else:
            for val in anslist:
                if val == -1:
                    self.minus += 1
                elif val == 0:
                    self.zero += 1
                elif val == 1:
                    self.plus += 1
            
            return -2

        
        
    def printAnswer(self):
        print(self.minus)
        print(self.zero)
        print(self.plus)
       

class InputClass:
    def __init__(self) -> None:
        self.string = ""
        self.li = []
        self.num = 0
        self.mainInput(5)
        
    def testInput(self,i):
        pass
            
    def caseInput(self,i):
        if i == 1:
            self.num = 4
            
    def mainInput(self, i):
        self.num = int(input().rstrip())
        for i in range(0,self.num):
            self.li.append(list(map(int, input().rstrip().split())))

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

r = PNumber()
r.printAnswer()