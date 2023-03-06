import random
import time


class SqPlus:
    def __init__(self, li) -> None:
        self.numlist = li
        self.plus_list = []
        self.minus_list = []
        self.answer = -1000
        self.pluster(self.numlist)

    def printAnswer(self):
        print(self.answer)

    def pluster(self, targetlist):
        is_tmp_positive = targetlist[0] >= 0
        tmp = 0
        pluslist=[]
        minuslist=[]

        # 더해서 각각 리스트화
        for i in targetlist:
            if i >= 0:
                is_pos = True
            else:
                is_pos = False
            
            if is_pos == is_tmp_positive:
                tmp += i
            else:
                if is_tmp_positive:
                    pluslist.append(tmp)
                    is_tmp_positive = False
                else:
                    minuslist.append(tmp)
                    is_tmp_positive = True
                tmp = i
        if is_tmp_positive:
            pluslist.append(tmp)
        else:
            minuslist.append(tmp)
        
        #함수 호출 전 사전 거르기
        if len(minuslist) == 0:
            self.answer = pluslist[0]
            return
        if len(pluslist) == 0:
            self.findAnswer(self.numlist)
            return
        if len(pluslist) == len(minuslist):
            if targetlist[0] < 0:
                minuslist.remove(minuslist[0])
            else:
                minuslist.remove(minuslist[len(minuslist) -1])
        if len(pluslist) < len(minuslist):
            minuslist.remove(minuslist[0])
            minuslist.remove(minuslist[len(minuslist) -1])

        # self.plus_list = pluslist
        # self.minus_list = minuslist

        self.crossPlus(pluslist, minuslist)

    def findAnswer(self, li):
        for i in li:
            if i > self.answer:
                self.answer = i

    def crossPlus(self, pluslist, minuslist):
        if len(minuslist) == 0:
            self.answer = pluslist[0]
            return

        maxindex = pluslist.index(max(pluslist))
        ad = 0
        
        tmplist = []
        for i in range(0, len(minuslist)):
            if i == maxindex:
                tmplist.append(pluslist[i])
                ad = 1
            tmplist.append(pluslist[i+ad] + minuslist[i])
        if not (len(tmplist) == len(pluslist)):
            tmplist.append(pluslist[len(pluslist) - 1])

        self.pluster(tmplist)


    def readyToAnswer(self):       
        is_calculating = True 
        cal = 0
        while(is_calculating):
            is_calculating = False            
            if len(self.minus_list) == 0:
                self.answer = self.plus_list[0]
                break
            #양수 기준 합치기
            for i in range(0, len(self.minus_list)):
                if self.plus_list[i] >= abs(self.minus_list[i]) and self.plus_list[i+1] >= abs(self.minus_list[i]):
                    tmp1 = self.plus_list[i] + self.plus_list[i+1] + self.minus_list[i]
                    self.plus_list[i] = 0
                    self.plus_list[i+1] = tmp1
                    self.minus_list[i] = 0
                    cal += 1
                    is_calculating = True
            if not(cal == 0):
                self.clearZero(cal)
                cal = 0
            # 양수 계산 한 번도 안 됐으면 음수 기준 합치기
            if not(is_calculating):
                for i in range(0,len(self.minus_list)-1):
                    if self.plus_list[i+1] < abs(self.minus_list[i]) and self.plus_list[i+1] < abs(self.minus_list[i+1]):
                        tmp2 = self.plus_list[i+1] + self.minus_list[i] + self.minus_list[i+1]
                        self.plus_list[i+1] = 0
                        self.minus_list[i] = 0
                        self.minus_list[i+1] = tmp2
                        cal += 1
                        is_calculating = True
                if not(cal == 0):
                    self.clearZero(cal)
                    cal = 0
           
        self.findAnswer(self.plus_list)

    def clearZero(self, cal):
        for i in range(0,cal):
                self.plus_list.remove(0)    
                self.minus_list.remove(0)

class InputClass:
    def __init__(self) -> None:
        self.li = []
        
        self.mainInput()

        # self.testInput()
        # print(self.li)

        #self.caseInput(3)

    def testInput(self):
        num = 100000
        for i in range(0,num):
            self.li.append(random.randint(-1000,1000))

    def caseInput(self,i):
        if i == 1:
            self.li = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
        if i == 2:
            self.li = [2, 1, -4, 3, 4, -4, 6, 5, -5, 1]
        if i == 3:
            self.li = [-1, -2, -3, -4, -5]

    def mainInput(self):
        num = int(input())
        self.li = input().split()

        for i in range(0,num):
            self.li[i] = int(self.li[i])

    def returnli(self):
        return self.li

i = InputClass()
li = i.returnli()

sq = SqPlus(li)
sq.printAnswer()
# ed = time.time()

# print(f"sec: {ed - st:.5f}")