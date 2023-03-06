import sys
input = sys.stdin.readline

class MatrixSquare:
    def __init__(self) -> None:
        inp = InputClass()
        self.MSlist = inp.returnli()
        self.numB = inp.returnnum()
        self.numN = len(self.MSlist)
        self.answer = []
        self.calculating()

    def calculating(self):
        if self.numB == 1:
            for i in range(0, len(self.MSlist)):
                for j in range(0, len(self.MSlist)):
                    self.MSlist[i][j] %= 1000
            self.answer = self.MSlist
        else:
            self.answer = self.divideConquer(self.numB)

    def divideConquer(self, depth) -> list:
        if depth == 1:
            return self.MSlist

        if depth % 2 > 0:
            return self.matrixMultiplication(self.divideConquer(depth - 1), self.MSlist)
        
        half = self.divideConquer(depth // 2)
        return self.matrixMultiplication(half, half)

    def matrixMultiplication(self, matrixA, matrixB) -> list:
        ans_matrix = []
        for n in range(0, self.numN):
            tmp = []
            for k in range(0, self.numN):
                attri = 0
                for m in range(0, self.numN):
                    attri = (attri + matrixA[n][m] * matrixB[m][k]) % 1000
                tmp.append(attri)
            ans_matrix.append(tmp.copy())
        return ans_matrix

      
    def printAnswer(self):
        for tmp in self.answer:
            for i in range(0,len(tmp)):
                if i == len(tmp)-1:
                    print(tmp[i], end="\n")
                    continue
                print(tmp[i], end=" ")


class InputClass:
    def __init__(self) -> None:
        self.string = ""
        self.li = []
        self.li2 = []
        self.num = 0
        self.mainInput(5)
        
    def testInput(self,i):
        pass
            
    def caseInput(self,i):
        if i == 1:
            self.num = 4
            
    def mainInput(self, i):
        tmp = list(map(int, input().rstrip().split()))
        self.num = tmp[1]
        for k in range(0, tmp[0]):
            self.li.append(list(map(int, input().rstrip().split())))

    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnli2(self) -> list:
        return self.li2

    def returnstring(self) -> str:
        return self.string

class TestCase:
    def __init__(self, fnc, numlist) -> None:
        self.fnc = fnc
        self.numlist = numlist

r = MatrixSquare()
r.printAnswer()