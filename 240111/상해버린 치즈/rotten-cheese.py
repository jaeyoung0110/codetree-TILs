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
for i in range(M) : # i : 상한치즈 idx
    data_s = [] # 상한거 먹은 사람 데이터 : [[사람, 배탈난 시간], ...]

    # 먹은 기록 탐색하면서 상한거 먹으면 data_s 추가
    for data in log_d :
        if data[1] == i :
            data_s.append([data[0],data[2]])
    
    # 실제 배탈 기록과 로그 배탈 기록 일치 확인
    is_ok = True
    for data in log_s :
        for k in data_s :
            if data[0] == k[0] :
                if data[1] <= k[1] :
                    is_ok = False
    
    # 가능한 케이스라면 배아픈 사람 수 구하기
    if is_ok == True :
        cnt_s = 0
        for data in log_d :
            if data[1] == i :
                cnt_s += 1
        ans_cnt = max(ans_cnt, cnt_s)

# 출력부
print(ans_cnt)