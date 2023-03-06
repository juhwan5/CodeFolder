class LongestIncreasingSubsequence:
    def __init__(self, li) -> None:
        self.LISlist = li   #1차원 배열
        self.answer = 0
        self.calculating()

    def calculating(self):
        anslist = []

        for i in range(0, len(self.LISlist)):
            ans = 1
            for j in range(0,i):
                if self.LISlist[i] <= self.LISlist[j]:
                    continue
                if ans <= anslist[j]:
                    ans += 1
            
            anslist.append(ans)

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
            self.li = [10,20,10,30,20,50]
        if i == 2:
            self.li = [1,2,3,9,4,5,6]

        if i == 10:
            self.li = [[4,7], [6,13], [4,8], [3,6], [5,12]]

    def mainInput(self,i):
        self.num = int(input())
        a = input().split()
        self.li = list(map(int, a))

    def returnli(self):
        return self.li

inp = InputClass(1)
li = inp.returnli()

r = LongestIncreasingSubsequence(li)
r.printAnswer()