class MRAssignment:
    def __init__(self) -> None:
        inp = InputClass()
        self.MRAlist = inp.returnli()
        self.MRAlist.sort(key= lambda x: (x[1],x[0]))
        self.answer = 0
        self.calculating()

    def calculating(self):
        endtime = 0
        for i in self.MRAlist:
            if i[0] >= endtime:
                self.answer += 1
                endtime = i[1]


    def printAnswer(self):
        print(self.answer)

class InputClass:
    def __init__(self) -> None:
        self.string = ""
        self.li = []
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
        self.num = int(input())
        for i in range(0, self.num):
            self.li.append(list(map(int,input().split())))
        

    def returnnum(self):
        return self.num

    def returnli(self):
        return self.li

    def returnstring(self):
        return self.string


r = MRAssignment()
r.printAnswer()