class ISum4:
    def __init__(self, li) -> None:
        self.IS4list = li.pop(0)
        self.Sumlist = li
        self.answer = []
        self.calculating()

    def calculating(self):
        anslist = [0]
        for i in range(0, len(self.IS4list)):
            tmp = anslist[i] + self.IS4list[i]
            anslist.append(tmp)

        for j in self.Sumlist:
            tmp = anslist[j[1]] - anslist[j[0] -1]
            self.answer.append(tmp)
            


    def printAnswer(self):
        for i in self.answer:
            print(i)

class InputClass:
    def __init__(self,num) -> None:
        self.li = []
        self.num = num
        self.mainInput(1)
        
    def testInput(self,i):
        pass

    def caseInput(self,i):
        if i == 1:
            self.li = [[5,4,3,2,1], [1,3], [2,4], [5,5]]

    def mainInput(self, i):
        fst = list(map(int, input().split()))
        
        scd = list(map(int, input().split()))
        self.li.append(scd)
        
        for i in range(0, fst[1]):
            trd = list(map(int, input().split()))
            self.li.append(trd)


    def returnli(self):
        return self.li

inp = InputClass(1)
li = inp.returnli()

r = ISum4(li)
r.printAnswer()