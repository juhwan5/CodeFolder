import sys
input = sys.stdin.readline

class SettingHR:
    def __init__(self) -> None:
        inp = InputClass()
        self.c = inp.returnnum()
        self.SHRlist = inp.returnli()
        self.SHRlist.sort()
        self.answer = 0
        self.calculating()

    def calculating(self):
        leng = self.SHRlist[len(self.SHRlist)-1] - self.SHRlist[0]
        upper = (leng // (self.c -1)) +1
        self.answer = upper
        downer = 0
        
        while(True):
            target = (upper + downer) //2
            if target == downer:
                self.answer = downer
                break

            if self.itsOK(target):
                downer = target
            else:
                upper = target


    def itsOK(self, num) -> bool:
        routers = 0
        now_house = 0
        for next_house in self.SHRlist:
            if routers == 0:
                now_house = next_house
                routers += 1
                continue

            if (next_house - now_house) >= num:
                now_house = next_house
                routers += 1
                if routers >= self.c:
                    return True

        return False




    def printAnswer(self):
        print(self.answer)

class InputClass:
    def __init__(self) -> None:
        self.string = ""
        self.li = []
        self.li2 = []
        self.num = 0
        self.mainInput(5)
        
    def testInput(self,i):
        pass
            
    def caseInput(self,i):
        if i == 1:
            self.num = 4
            
    def mainInput(self, i):
        a, self.num = list(map(int, input().rstrip().split()))
        for i in range(0, a):
            self.li.append(int(input().rstrip()))
        
    def returnnum(self) -> int:
        return self.num

    def returnli(self) -> list:
        return self.li

    def returnli2(self) -> list:
        return self.li2

    def returnstring(self) -> str:
        return self.string

class TestCase:
    def __init__(self, fnc, numlist) -> None:
        self.fnc = fnc
        self.numlist = numlist

r = SettingHR()
r.printAnswer()