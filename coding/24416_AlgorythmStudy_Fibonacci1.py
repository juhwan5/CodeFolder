class AlgorythmFibo1:
    def __init__(self, num) -> None:
        self.num = num
        self.code1_runtime = 0
        self.code2_runtime = 0
        #self.fib1 = self.doFib1(self.num)
        self.fib2 = self.doFib2(self.num)


    def printAnswer(self):
        print(self.code1_runtime)
        print(self.code2_runtime)

    def printA(self):
        print(self.fib2)

    def doFib1(self,num):
        if(num <= 2):
            self.code1_runtime += 1
            return 1
        else:
            return self.doFib1(num-1) + self.doFib1(num - 2)

    def doFib2(self, num):
        templist = [1,1]
        for i in range(2, num):
            self.code2_runtime += 1
            fib = templist[i -1] + templist[i-2]
            templist.append(fib)
    
        return templist[num -1]


a = int(input())
b = AlgorythmFibo1(a+1)
b.printA()