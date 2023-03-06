class RGBSt:
    def __init__(self, li) -> None:
        self.RGBit = [0,1,2]
        self.RGBlist = li   #2차원 배열
        self.answer = 0
        self.calculating()

    def calculating(self):
        anslist = []

        for rgb_value in self.RGBlist:
            newlist = []
            if len(anslist) == 0:
                anslist = rgb_value.copy()
                continue

            for i in range(0,3):
                tmp = anslist.copy()
                tmp[i] = 10000000
                newlist.append(rgb_value[i] + min(tmp))
            
            anslist = newlist.copy()

        self.answer = min(anslist)

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
            self.li = [ [26, 40, 83] , [49, 60, 57], [13, 89, 99]]
            return
        if i == 2:
            self.li = [ [1, 100, 100] , [100,1,100], [100,100,1]]
            return
        if i == 3:
            self.li = [ [1,100,100] , [100,100,100], [1,100,100]]
            return
        if i == 4:
            self.li = [ [30,19,5] , [64,77,64], [15,19,97], [4,71,57], [90,86,84], [93,32,91]]
            return
        if i == 5:
            self.li = [ [71,39,44], [32,83,55], [51,37,63], [89,29,100], [83,58,11], [65,13,15], [47,25,29], [60,66,19]]
            return

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

r = RGBSt(li)
r.printAnswer()