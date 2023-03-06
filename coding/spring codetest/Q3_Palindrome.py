def solution(queries):
    answer = []
    if len(queries[0]) %2 == 0:
        for query in queries:
            summery = sum(query)
            if summery % 2 == 0:
                answer.append(0)
            else:
                answer.append(1)
    else:
        for query in queries:
            mid = query[len(query)//2]
            summery = sum(query) - mid
            if summery % 2 == 0:
                if mid % 2 == 0:
                    answer.append(0)
                else:
                    answer.append(1)
            else:
                idx = 0
                checker = True
                while(idx == mid):
                    if (query[idx] == query[len(query) - idx -1]) or checker:
                        pass
                    else:
                        if checker:
                            checker = False
                        else:
                            break
                    idx += 1
                if idx == mid:
                    answer.append(1)
                    continue

                if mid % 2 == 0:
                    answer.append(1)
                else:
                    answer.append(0)

    return answer

lo = [[2,3,6], [1,2,5], [1,2,3,4,5]]
ans = solution(lo)
print(ans)