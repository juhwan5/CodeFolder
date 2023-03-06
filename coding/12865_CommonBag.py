class CommonBag:
    def __init__(self, li) -> None:
        first = li.pop(0)
        self.limit_weight = first[1]
        self.CBlist = li   #2차원 배열
        self.answer = 0
        self.calculating()

    def calculating(self):
        a = "0" * (self.limit_weight+1)
        anslist = list(map(int, a))

        for i in range(0, len(self.CBlist)):
            tmplist = []

            wei = self.CBlist[i][0]
            val = self.CBlist[i][1]

            not_overweight = True
            for j in range(0, len(anslist)):
                if not_overweight:
                    if (j+1) == wei:
                        not_overweight = False
                    tmp = anslist[j]
                else:
                    tmp = max(anslist[j], anslist[j-wei] + val)
                

                tmplist.append(tmp)

            anslist = tmplist.copy()

        self.answer = max(anslist)
            

    def printAnswer(self):
        print(self.answer)

class InputClass:
    def __init__(self,num) -> None:
        self.li = []
        self.num = 1
        self.mainInput(2)
        
    def testInput(self,i):
        pass

    def caseInput(self,i):
        if i == 1:
            self.li = [[4,7], [6,13], [4,8], [3,6], [5,12]]
        if i == 2:  #답 17
            self.li = [[10, 15], [1,1], [2,3], [5,3], [5,1], [4,5], [3,3], [3,2], [4,4], [4,4], [4,3]]
        
        

    def mainInput(self,i):
        a = input().split()
        li = list(map(int, a))
        self.li.append(li)

        for i in range(0, li[0]):
            b = input().split()
            li = list(map(int, b))
            self.li.append(li)
            

    def returnli(self):
        return self.li

inp = InputClass(1)
li = inp.returnli()

r = CommonBag(li)
r.printAnswer()