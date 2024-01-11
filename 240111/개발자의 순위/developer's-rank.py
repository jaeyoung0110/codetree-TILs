# 변수 설정 및 입력부 처리
K, N = map(int,input().split())
log = []
for _ in range(K) :
    log.append(list(map(int,input().split())))

ans_cnt = 0

# 알고리즘
# 두명 선택 완전탐색
for i in range(1,N+1) :
    for j in range(1,N+1) :
        is_ok = True
        for data in log :
            if data.index(i) >= data.index(j) :
                is_ok = False
        if is_ok == True :
            ans_cnt += 1
    
print(ans_cnt)