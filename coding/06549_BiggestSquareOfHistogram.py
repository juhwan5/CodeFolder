import sys
input = sys.stdin.readline

class BSofHistogram:
    def __init__(self) -> None:
        inp = InputClass()
        self.BSlist = inp.returnli()
        self.answer = []
        self.calculating()

    def calculating(self):
        for bs in self.BSlist:
            ans = self.divideConquer(bs)
            self.answer.append(ans)

    def divideConquer(self, lx:list) -> int:
        if len(lx) == 1:
            return lx[0]
        
        mid = len(lx) // 2
        leftmax = self.divideConquer(lx[:mid])
        rightmax = self.divideConquer(lx[mid:])

        midmax = 0
        lidx = mid - 1
        ridx = mid
        height = 1000000000
        is_left_ok = True
        is_right_ok = True
        while(True):
            if not(is_left_ok) and not(is_right_ok):
                return max(leftmax, rightmax, midmax)
            height = min(height, lx[lidx], lx[ridx])
            tmp = (ridx - lidx +1) * height
            midmax = max(midmax, tmp)
            
            if lidx - 1 < 0:
                is_left_ok = False
            if ridx + 1 >= len(lx):
                is_right_ok = False
            
            if is_left_ok and is_right_ok:
                if lx[lidx -1] >= lx[ridx +1]:
                    lidx -= 1
                else:
                    ridx += 1
            elif is_left_ok or is_right_ok:
                if is_left_ok:
                    lidx -= 1
                else:
                    ridx += 1
            
      
    def printAnswer(self):
        for i in self.answer:
            print(i)


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
        while(True):
            tmp = list(map(int, input().rstrip().split()))
            if tmp[0] == 0:
                break
            self.li.append(tmp[1:].copy())

             

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

r = BSofHistogram()
r.printAnswer()