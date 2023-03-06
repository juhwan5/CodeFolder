import sys
input = sys.stdin.readline

class MatrixSquare:
    def __init__(self) -> None:
        inp = InputClass()
        self.num = inp.returnnum()
        self.answer = 0
        self.modnum = 1000000007
        self.matrix = [[1,1],[1,0]]
        self.calculating()

    def calculating(self):
        if self.num == 1:
            self.answer = 1
        else:
            li = [[1],[0]]
            ans = self.matrixMultiplication(self.divideConquer(self.num - 1), li)
            self.answer = ans[0][0]

    def divideConquer(self, depth) -> list:
        if depth == 1:
            return self.matrix

        if depth % 2 > 0:
            return self.matrixMultiplication(self.divideConquer(depth - 1), self.matrix)
        
        half = self.divideConquer(depth // 2)
        return self.matrixMultiplication(half, half)

    def matrixMultiplication(self, matrixA, matrixB) -> list:
        ans_matrix = []
        numN = len(matrixA)
        numM = len(matrixA[0])
        numK = len(matrixB[0])
        for n in range(0, numN):
            tmp = []
            for k in range(0, numK):
                attri = 0
                for m in range(0, numM):
                    attri = (attri + matrixA[n][m] * matrixB[m][k]) % self.modnum
                tmp.append(attri)
            ans_matrix.append(tmp.copy())
        return ans_matrix

      
    def printAnswer(self):
        print(self.answer)


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
        self.num = int(input().rstrip())

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