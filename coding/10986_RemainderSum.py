class RSum:
    def __init__(self) -> None:
        inp = InputClass()
        self.RSlist = inp.returnli()
        self.num = inp.returnnum()
        self.answer = 0
        self.calculating()

    def calculating(self):
        ans = 0
        ansdict = {0:0}
        for i in range(0, len(self.RSlist)):
            tmp = (self.RSlist[i] + ans) % self.num
            
            if tmp in ansdict:
                ansdict[tmp] += 1
            else:
                ansdict[tmp] = 1
            ans = tmp
        
        self.answer += ansdict[0]
        for idx in ansdict:
            val = ansdict[idx]
            if val >= 2:
                sum = (val * (val-1) // 2)
                self.answer += sum



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
            self.num = 3
            self.li = [1,2,3,1,2]
        if i == 2:
            self.num = 10
            self.li = [5,8,2,5,9,3,2,7,9,6]


    def mainInput(self, i):
        a = list(map(int, input().split()))
        self.num = a[1]
        self.li = list(map(int, input().split()))

    def returnnum(self):
        return self.num

    def returnli(self):
        return self.li

    def returnstring(self):
        return self.string


r = RSum()
r.printAnswer()