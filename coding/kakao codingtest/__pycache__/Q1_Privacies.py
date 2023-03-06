def solution(today:str, terms:list[str], privacies:list[str]):
    answer = []
    todaydate = DateC(today)
    termsdict = {}
    for i in terms:
        key, t = i.split()
        termsdict[key] = int(t)

    num = 1
    for i in privacies:
        datetxt, term = i.split()
        dateC = DateC(datetxt)
        dateC.calculTerms(termsdict[term])

        if (dateC.isthisPTrash(todaydate)):
            answer.append(num)
        num += 1

    return answer

class DateC:
    def __init__(self, datetxt: str) -> None:
        ymd = list(map(int, datetxt.split(".")))
        self.Y = ymd[0]
        self.M = ymd[1]
        self.D = ymd[2]

    def calculTerms(self, mon:int) -> None:
        #일 계산
        self.D -= 1
        if self.D <= 0:
            self.D += 28
            self.M -= 1
        #월 계산
        self.M += mon
        if self.M > 12:
            if self.M % 12 ==0:
                self.Y += (self.M - 12) // 12
                self.M = 12
            else:
                self.Y += self.M //12
                self.M %= 12


    def isthisPTrash(self, today: 'DateC') -> bool:
        if self.Y < today.Y:
            return True
        elif self.Y > today.Y:
            return False
        else:
            if self.M < today.M:
                return True
            elif self.M > today.M:
                return False
            else:
                if self.D < today.D:
                    return True
                else:
                    return False
                
      