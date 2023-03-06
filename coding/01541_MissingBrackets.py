class MBrackets:
    def __init__(self) -> None:
        inp = InputClass()
        self.MBlist = inp.returnstring()
        self.li = inp.returnli()
        self.answer = 0
        self.calculating()

    def calculating(self):
        numlist = []
        callist = []
        num = 0
        for i in self.MBlist:
            if i == "+":
               numlist.append(num)
               num = 0
               callist.append(1)
            elif i == "-":
               numlist.append(num)
               num = 0
               callist.append(-1)
            else:
                a = int(i)
                num = (num*10) + a
        numlist.append(num)

        nowsum = numlist[0]
        not_minus = True
        for i in range(0, len(callist)):
            if callist[i] == -1:
                not_minus = False
            
            if not_minus:
                nowsum += numlist[i+1]
            else:
                nowsum -= numlist[i+1]
        
        self.answer = nowsum

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
            self.string = "55-50+40" #-35
        if i == 2:
            self.string = "10+20+30+40" #100
            self.num = 10
            self.li = [5,8,2,5,9,3,2,7,9,6]
        if i == 3:
            self.string = "00009-00009" #0


    def mainInput(self, i):
        self.string = input()
        
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnstring(self) -> str:
        return self.string


r = MBrackets()
r.printAnswer()