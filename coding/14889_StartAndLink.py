import MyUtility

class StartAndLink():
    def __init__(self,num_of_people, ability_array) -> None:
        self.num_of_people = num_of_people
        self.ability_array = ability_array
        

    def doItAndAnswer(self) -> None:
        my_answer = self.doIt()
        print(my_answer)

    def doIt(self):

        the_answer = 100000
        #팀짜기
        personnol_array = []   #size = personnol - 1, 0이 없는 배열
        for i in range(1, self.num_of_people):
            personnol_array.append(i)
        comb = MyUtility.CombinationClass(personnol_array, self.num_of_people /2 -1)
        cases = comb.getCases()

        personnol_array.append(0)
        for one_of_case in cases:
            start_team = one_of_case.copy()
            start_team.append(0)
            link_team = personnol_array.copy()
            for i in start_team:
                link_team.remove(i)
            # 능력치 합산
            start_team_ability = self.abilityChecking(start_team)
            link_team_ability = self.abilityChecking(link_team)

            new_answer = abs(start_team_ability - link_team_ability)

            if the_answer > new_answer:
                the_answer = new_answer

        return the_answer

    def abilityChecking(self, target):
        all_ability = 0
        for i in range(0,len(target)):
            for j in range(i+1,len(target)):
                a = target[i]
                b = target[j]
                all_ability = all_ability + int(self.ability_array[a][b]) + int(self.ability_array[b][a])

        return all_ability


def MainMethod():
    num_of_people = int(input())
    if((num_of_people % 2) != 0):
        print("num_of_people Error")
        return
    
    ability_array = []

    for i in range(0,num_of_people):
        temp_array = input().split()
        ability_array.append(temp_array.copy())

    class_instance = StartAndLink(num_of_people, ability_array)
    class_instance.doItAndAnswer()

    
MainMethod()