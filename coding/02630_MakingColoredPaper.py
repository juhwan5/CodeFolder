import sys
input = sys.stdin.readline

class MakingCP:
    def __init__(self) -> None:
        inp = InputClass()
        self.num = inp.returnnum()
        self.MCPlist = inp.returnli()
        self.white = 0
        self.blue = 0
        self.calculating()

    def calculating(self):
        tmp = self.divideConquer(0,0, len(self.MCPlist[0]))
        if tmp == 0:
            self.white += 1
        elif tmp == 1:
            self.blue += 1

    def divideConquer(self, col_start, row_start, given_length) -> int:
        if given_length == 1:
            return self.MCPlist[col_start][row_start]
        
        now_length : int = given_length // 2
        part_a = self.divideConquer(col_start, row_start, now_length)
        part_b = self.divideConquer(col_start + now_length, row_start, now_length)
        part_c = self.divideConquer(col_start, row_start + now_length, now_length)
        part_d = self.divideConquer(col_start + now_length, row_start + now_length, now_length)

        if part_a == part_b == part_c == part_d and part_a != -1:
            return part_a
        else:
            for pt in [part_a, part_b, part_c, part_d]:
                if pt == 0:
                    self.white += 1
                elif pt == 1:
                    self.blue += 1
            return -1

        
    def printAnswer(self):
        print(self.white)
        print(self.blue)

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

r = MakingCP()
r.printAnswer()