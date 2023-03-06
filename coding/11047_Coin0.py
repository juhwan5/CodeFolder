class Coin0:
    def __init__(self) -> None:
        inp = InputClass()
        self.Coin0list = inp.returnli()
        self.Coin0list.reverse()
        self.num = inp.returnnum()
        self.answer = 0
        self.calculating()

    def calculating(self):
        val = self.num
        for i in self.Coin0list:
            if (val // i) > 0:
                self.answer += val // i
                val = val % i
                if val == 0:
                    break

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
        a = list(map(int, input().split()))
        self.num = a[1]
        for i in range(0, a[0]):
            self.li.append(int(input()))
        

    def returnnum(self):
        return self.num

    def returnli(self):
        return self.li

    def returnstring(self):
        return self.string


r = Coin0()
r.printAnswer()