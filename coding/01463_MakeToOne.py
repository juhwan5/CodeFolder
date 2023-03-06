class MTOne:
    def __init__(self, num) -> None:
        self.num = num
        self.calculed = [0,0,1,1]
        self.answer = 0

        self.calculating()

    def calculating(self):
        for i in range(4, self.num+1):
            candidate = []
            candidate.append(self.calculed[i-1])
            if (i%2) == 0:
                candidate.append(self.calculed[i//2])
            if (i%3) == 0:
                candidate.append(self.calculed[i//3])

            self.calculed.append(min(candidate) + 1)
        self.answer = self.calculed[self.num]

    def printAnswer(self):
        print(self.answer)


a = int(input())

r = MTOne(a)
r.printAnswer()
