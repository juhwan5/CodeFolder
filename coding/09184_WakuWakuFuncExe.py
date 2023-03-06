class Stacker:
    def __init__(self) -> None:
        self.stack1 = {1: {1: {1:2} } }

    def searchValue(self, a, b, c):
        if a in self.stack1:
            stack2 = self.stack1[a]
            if b in stack2:
                stack3 = stack2[b]
                if c in stack3:
                    return stack3[c]
        return None

    def addValue(self, a, b, c, the_value):
        if not(a in self.stack1):
            self.stack1[a] = {b: {c : the_value}}
            return
        stack2 = self.stack1[a]
        if not(b in stack2):
            stack2[b] = {c : the_value}
            return
        stack3 = stack2[b]
        if not(c in stack3):
            stack3[c] = the_value
        
    def wf(self, a, b, c):
        #하나라도 양수가 아니라면 1
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        #하나라도 20을 넘으면 20으로 초기화
        if a > 20 or b > 20 or c >20:
            return self.wf(20, 20, 20)
        exist_value = self.searchValue(a,b,c)
        #계산한 적 있다면 반환
        if not(exist_value is None):
            return exist_value
        #없으면 첫번째 조건의 계산
        if a<b and b<c:
            calcul_value = self.wf(a,b,c-1) + self.wf(a,b-1,c-1) - self.wf(a, b-1, c)
            self.addValue(a,b,c, calcul_value)
            return calcul_value
        
        #다 없으면 두번째 조건의 계산
        calcul_value = self.wf(a-1, b, c) + self.wf(a-1, b-1, c) + self.wf(a-1, b, c-1) - self.wf(a-1, b-1, c-1)
        self.addValue(a,b,c, calcul_value)
        return calcul_value


class InputClass:
    def inputMethod(self):
        endbit = True
        templist = []

        while(endbit):
            li = input().split()
            for i in range(0,3):
                li[i] = int(li[i])
            if(li[0]== -1 and li[1]== -1 and li[2]== -1):
                endbit = False
                continue
            templist.append(li.copy())
        return templist

    def testMethod(self):
        templist = [[1,1,1], [2,2,2],[10,4,6],[50,50,50],[-1,7,18]]
        return templist


inp = InputClass()
templist = inp.inputMethod()

st = Stacker()
for tmp in templist:
    prt = st.wf(tmp[0], tmp[1], tmp[2])
    print(f"w({tmp[0]}, {tmp[1]}, {tmp[2]}) = {prt}")