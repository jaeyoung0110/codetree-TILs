# 입력부
N, M, D, S = map(int,input().split())

log_d = []
for _ in range(D) :
    log_d.append(list(map(int,input().split())))

log_s = []
for _ in range(S) :
    log_s.append(list(map(int,input().split())))


# 알고리즘
# 각 치즈가 상한 경우 완전탐색으로 각 치즈로 상했을 때 먹은 기록을 바탕으로 배탈난 기록과 같으면 그 케이스가 답
ans_cnt = 0
for i in range(1,M+1) : # i : 상한치즈 idx
    data_s = [] # 상한거 먹은 사람 데이터 : [[사람, 배탈난 시간], ...]

    # 먹은 기록 탐색하면서 상한거 먹으면 data_s 추가
    for data in log_d :
        if data[1] == i :
            is_dup = False
            for v in data_s :
                if v[0] == data[0] :
                    is_dup = True
                    if v[1] > data[2] :
                        v[1] = data[2]
            if is_dup == False :
                data_s.append([data[0],data[2]])
                        
                
    # print("i, data_s: ", i, data_s)
    # 실제 배탈 기록과 로그 배탈 기록 일치 확인
    is_ok = True
    for data in log_s :
        # 만약 data[0] 사람이 data_s 에 안들어있으면 is_ok False
        is_in = False
        for k in data_s :
            if data[0] == k[0] :
                is_in = True
        if is_in == False :
            is_ok = False
            break
        for k in data_s :
            if data[0] == k[0] :
                if data[1] <= k[1] :
                    is_ok = False
                    break

    
    # 가능한 케이스라면 배아픈 사람 수 구하기
    if is_ok == True :
        # print(i, end=' ')
        cnt_s = []
        for data in log_d :
            if data[1] == i :
                if data[0] not in cnt_s :
                    cnt_s.append(data[0])
        # print(cnt_s)
        ans_cnt = max(ans_cnt, len(cnt_s))

# 출력부
print(ans_cnt)