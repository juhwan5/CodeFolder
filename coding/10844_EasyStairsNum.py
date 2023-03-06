from re import L


class ESNum:
    def __init__(self, num) -> None:
        self.num = num
        self.answer = 0
        self.calculating()

    def calculating(self):
        anslist = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        for round in range(1,self.num):
            newlist = []
            for i in range(0,10):
                if i == 0:
                    newlist.append(anslist[i+1])
                elif i == 9:
                    newlist.append(anslist[i-1])
                else:
                    newlist.append(anslist[i-1] + anslist[i+1])
            
            for i in range(0, 10):
                newlist[i] %= 1000000000

            anslist = newlist.copy()

        self.answer = sum(anslist) % 1000000000


    def printAnswer(self):
        print(self.answer)

li = int(input())

r = ESNum(li)
r.printAnswer()