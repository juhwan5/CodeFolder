class HCInteraction:
    def __init__(self) -> None:
        inp = InputClass()
        self.HCIlist = inp.returnli()
        self.string = inp.returnstring()
        self.answer = []
        self.calculating()

    def calculating(self):
        a = "0" * 26
        prelist = list(map(int,a))

        anslist = []
        anslist.append(prelist.copy())
        for i in self.string:
            idx = ord(i) - 97
            prelist[idx] += 1
            anslist.append(prelist.copy())
        
        for i in self.HCIlist:
            spell, st, ed = ord(i[0])-97, i[1], i[2]
            ans = anslist[ed+1][spell] - anslist[st][spell]
            self.answer.append(ans)

        
    def printAnswer(self):
        for i in self.answer:
            print(i)

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
            self.string = "seungjaehwang"
            self.li = [["a",0,5], ["a",0,6], ["a",6,10], ["a",7,10]]

    def mainInput(self, i):
        self.string = input()
        self.num = int(input())
        for i in range(0, self.num):
            tmp = input().split()
            for j in range(1,3):
                tmp[j] = int(tmp[j])
            self.li.append(tmp)


    def returnnum(self):
        return self.num

    def returnli(self):
        return self.li

    def returnstring(self):
        return self.string


r = HCInteraction()
r.printAnswer()