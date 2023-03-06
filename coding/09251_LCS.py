class LongestCommonSubsequence:
    def __init__(self, li) -> None:
        self.rowlist = li[0]        #기준 문자열
        self.columnlist = li[1]     #매길 대상
        self.answer = 0
        self.calculating()

    def calculating(self):
        anslist = [0]
        for i in range(0, len(self.columnlist)):
            anslist.append(0)

        for i in range(0, len(self.rowlist)):
            tmplist = [0]
            for j in range(0, len(self.columnlist)):
                if self.rowlist[i] == self.columnlist[j]:
                    tmp = anslist[j] + 1
                else:
                    tmp = max(anslist[j+1], tmplist[j])
                tmplist.append(tmp)
            
            anslist = tmplist.copy()

        self.answer = max(anslist)

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
            self.li = ["ACAYKP", "CAPCAK"]

    def mainInput(self,i):
        for i in range(0,2):
            a = input()
            self.li.append(a)

    def returnli(self):
        return self.li

inp = InputClass(1)
li = inp.returnli()

r = LongestCommonSubsequence(li)
r.printAnswer()