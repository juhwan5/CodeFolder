class NNTri:
    def __init__(self, li) -> None:
        self.ntlist = li   #2차원 배열
        self.answer = 0
        self.calculating()

    def calculating(self):
        anslist = []

        for nt_value in self.ntlist:
            newlist = []
            if len(anslist) == 0:
                anslist = nt_value.copy()
                continue

            for i in range(0,len(nt_value)):
                if i == 0:
                    newlist.append(anslist[i] + nt_value[i])
                elif i == (len(nt_value) - 1):
                    newlist.append(anslist[i-1] + nt_value[i])
                else:
                    newlist.append(nt_value[i] + max(anslist[i-1], anslist[i]))
            
            anslist = newlist.copy()

        self.answer = max(anslist)

    def printAnswer(self):
        print(self.answer)

class InputClass:
    def __init__(self,num) -> None:
        self.li = []
        self.num = num
        self.mainInput()
        
    def testInput(self):
        pass

    def caseInput(self,i):
        if i == 1:
            self.li = [[7], [3,8], [8,1,0], [2,7,4,4], [4,5,2,6,5]]

    def mainInput(self):
        self.num = int(input())

        for i in range(0,self.num):
            a = input().split()
            b = []
            for i in a:
                b.append(int(i))
            self.li.append(b)

    def returnli(self):
        return self.li

inp = InputClass(1)
li = inp.returnli()

r = NNTri(li)
r.printAnswer()