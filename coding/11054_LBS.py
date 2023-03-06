class LongestBitonicSubsequence:
    def __init__(self, li) -> None:
        self.LBSlist = li   #1차원 배열
        self.answer = 0
        self.calculating()

    def calculating(self):
        uplist = []
        downlist = []
        anslist = []
        reLBSlist = self.LBSlist.copy()
        reLBSlist.reverse()

        for i in range(0, len(self.LBSlist)):
            ans = 1
            for j in range(0,i):
                if self.LBSlist[i] <= self.LBSlist[j]:
                    continue
                if ans <= uplist[j]:
                    ans += 1
            
            uplist.append(ans)

        for i in range(0, len(reLBSlist)):
            ans = 1
            for j in range(0,i):
                if reLBSlist[i] <= reLBSlist[j]:
                    continue
                if ans <= downlist[j]:
                    ans += 1
            
            downlist.append(ans)
        
        downlist.reverse()

        for i in range(0, len(self.LBSlist)):
            anslist.append(uplist[i] + downlist[i] - 1)

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
            self.li = [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]
        if i == 2:
            self.li = [1,2,3,9,4,5,6]

    def mainInput(self,i):
        self.num = int(input())
        a = input().split()
        for i in a:
            self.li.append(int(i))

    def returnli(self):
        return self.li

inp = InputClass(1)
li = inp.returnli()

r = LongestBitonicSubsequence(li)
r.printAnswer()