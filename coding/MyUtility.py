import time
import random

class CombinationClass:
    def __init__(self, target_array, num_of_combination) -> None:
        self.target_array = target_array
        self.num_of_combination = num_of_combination
        self.cases = []
        self.combinating([],0)

    
    def combinating(self, selected_things, first_index):
        if len(selected_things) == self.num_of_combination:
            self.cases.append(selected_things)
        else:
            for i in range(first_index, len(self.target_array)):
                s_t_copy = selected_things.copy()
                s_t_copy.append(self.target_array[i])
                self.combinating(s_t_copy, i+1)

    def printing(self):
        print(self.cases)

    def getCases(self):
        return self.cases

class SortingMethod:
    def lambdasorting():
        li = []
        li.sort(key= lambda x:(x[1], x[0]))

class TimeCheck:
    def timing():
        st = time.time()
        ed = time.time()
        print(f"sec: {ed - st:.5f}")


class InputClass:
    def __init__(self) -> None:
        self.li = []    # 1차원 배열
        self.num = 1
        self.mainInput(1)
        
    def testInput(self,i):
        if i == 1:
            self.li = [1,2,3,4,5]
        if i == 2:
            pass

    def caseInput(self,i):
        a = random.randint(0,10)

    def mainInput(self, i):
        self.num = int(input())
        
        for i in range(0, self.num):
            a = input().split
            self.li.append(list(map(int, a)))

    def returnli(self):
        return self.li