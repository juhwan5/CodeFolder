def solution(lotteries):
    
    percentages = []
    for lottery in lotteries:
        per = lottery[0] / (lottery[1] +1)
        if per > 1:
            per = 1
        percentages.append(per)
    
    top_percent = max(percentages)
    idxes = []
    ans = []
    for num in range(len(lotteries)):
        if percentages[num] == top_percent:
            idxes.append(num+1)
            ans.append(lotteries[num][2])
    
    answer = idxes[ans.index(max(ans))]
    return answer



lo = [[100,100,500],[1000,1000,100]]
ans = solution(lo)
print(ans)