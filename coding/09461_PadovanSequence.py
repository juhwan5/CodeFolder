class Padovan:
    def __init__(self) -> None:
        self.tri = [1,1,1,2,2]

    def pn(self,num):
        for i in range(len(self.tri), num):
            val = self.tri[i-1] + self.tri[i-5]
            self.tri.append(val)

        return self.tri[num-1]

p = Padovan()
a = int(input())
b = []

for i in range(0,a):
    tmp = int(input())
    b.append(tmp)


for i in range(0,a):
    print(p.pn(b[i]))

