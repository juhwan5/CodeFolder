class Sequence:
    def __init__(self, num, li) -> None:
        self.num = num
        self.Sqlist = li
        self.answer = 0
        self.calculating()

    def calculating(self):
        anslist = []
        ans = 0
        for i in range(0, self.num):
            ans += self.Sqlist[i]
        anslist.append(ans)

        cir = len(self.Sqlist) - self.num
        for i in range(0, cir):
            ans = anslist[i] - self.Sqlist[i] + self.Sqlist[i+self.num]
            anslist.append(ans)

        self.answer = max(anslist)
        

    def printAnswer(self):
        print(self.answer)

class InputClass:
    def __init__(self,num) -> None:
        self.li = []
        self.num = num
        self.mainInput(1)
        
    def testInput(self,i):
        pass

    def caseInput(self,i):
        if i == 1:
            self.li = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]

    def mainInput(self, i):
        a = list(map(int, input().split()))
        self.num = a[1]
        self.li = list(map(int, input().split()))

    def returnnum(self):
        return self.num

    def returnli(self):
        return self.li

inp = InputClass(1)
nu = inp.returnnum()
li = inp.returnli()

r = Sequence(nu,li)
r.printAnswer()