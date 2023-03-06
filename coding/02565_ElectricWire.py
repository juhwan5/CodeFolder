class EWire:
    def __init__(self, li = []) -> None:
        self.EWlist = li   #2차원 배열
        self.answer = 0
        self.targetlist = []
        self.createTarget()
        self.calculating()

    def createTarget(self):
        a = self.EWlist.copy()
        a.sort()
        for i in a:
            self.targetlist.append(i[1])

    def calculating(self):
        anslist = []

        for i in range(0, len(self.targetlist)):
            ans = 1
            for j in range(0,i):
                if self.targetlist[i] <= self.targetlist[j]:
                    continue
                if ans <= anslist[j]:
                    ans += 1
            
            anslist.append(ans)

        self.answer = len(anslist) - max(anslist)

    def printAnswer(self):
        print(self.answer)

class InputClass:
    def __init__(self,num) -> None:
        self.li = []
        self.num = 1
        self.mainInput(1)
        
    def testInput(self,i):
        pass

    def caseInput(self,i):
        if i == 1:
            self.li = [[1,8], [3,9], [2,2], [4,1], [6,4], [10,10], [9,7], [7,6]]
        if i == 2:
            self.li = [1,2,3,9,4,5,6]

    def mainInput(self,i):
        self.num = int(input())
        

        for i in range(0, self.num):
            a = input().split()
            for i in range(0,2):
                a[i] = int(a[i])
            self.li.append(a)

    def returnli(self):
        return self.li

inp = InputClass(1)
li = inp.returnli()

r = EWire(li)
r.printAnswer()