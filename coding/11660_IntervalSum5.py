class ISum5:
    def __init__(self) -> None:
        inp = InputClass()
        self.IS5list = inp.returnli()
        self.qu = inp.returnqu()
        self.num = inp.returnnum()
        self.answer = []
        self.calculating()

    def calculating(self):
        a = "0" * (self.num + 1)
        tmplist = list(map(int, a))
        anslist = []
        anslist.append(tmplist.copy())
        for xidx in range(0, self.num):
            tmplist = [0]
            prelist = anslist[xidx]
            xlist = self.IS5list[xidx]
            for yidx in range(0, self.num):
                tmp = xlist[yidx] + tmplist[yidx] + prelist[yidx+1] - prelist[yidx]
                tmplist.append(tmp)
            anslist.append(tmplist.copy())

        for qu in self.qu:
            x1,y1,x2,y2 = qu[0]-1, qu[1]-1, qu[2], qu[3]
            ans = anslist[x2][y2] - anslist[x1][y2] - anslist[x2][y1] + anslist[x1][y1]
            self.answer.append(ans)



    def printAnswer(self):
        for i in self.answer:
            print(i)

class InputClass:
    def __init__(self) -> None:
        self.string = ""
        self.li = []
        self.qu = []
        self.num = 0
        self.mainInput(1)
        
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
        self.num = a[0]
        for i in range(0, self.num):
            b = list(map(int, input().split()))
            self.li.append(b)
        
        for j in range(0, a[1]):
            b = list(map(int, input().split()))
            self.qu.append(b)


    def returnnum(self):
        return self.num

    def returnli(self):
        return self.li

    def returnqu(self):
        return self.qu

    def returnstring(self):
        return self.string


r = ISum5()
r.printAnswer()