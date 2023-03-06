def solution(cap, n, deliveries, pickups):
    dp_idx = [n-1, n-1]
    max_idx = max(dp_idx)
    deli_pick_list = [deliveries, pickups]
    answer = 0

    while(max_idx >= 0):
        # 제일 먼 곳 확인
        for i in range(0,2):
            while(dp_idx[i]>= 0):
                if deli_pick_list[i][dp_idx[i]] == 0:
                    dp_idx[i] -= 1
                    continue
                else:
                    break

        # 목표 설정 후 거리 계산
        max_idx = max(dp_idx)
        if max_idx < 0:
            break
        answer += (max_idx + 1) * 2

        # 배달/수거 작업
        for i in range(0,2):
            rest_space = cap
            while(rest_space > 0 and dp_idx[i] >= 0):
                if deli_pick_list[i][dp_idx[i]] >= rest_space:
                    deli_pick_list[i][dp_idx[i]] -= rest_space
                    rest_space = 0
                else:
                    rest_space -= deli_pick_list[i][dp_idx[i]]
                    deli_pick_list[i][dp_idx[i]] = 0
                    dp_idx[i] -= 1

    return answer