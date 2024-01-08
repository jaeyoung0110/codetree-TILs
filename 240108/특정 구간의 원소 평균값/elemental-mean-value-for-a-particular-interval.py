N = int(input())
arr = list(map(int,input().split()))

ans_cnt = 0

for i in range(N) :
    for j in range(i, N) :
        # 구간 크기 0 이면 그냥 맞음
        if i == j :
            ans_cnt += 1
            continue

        # 평균 구하기
        mean_cnt = 0
        for k in range(i,j+1) :
            mean_cnt += arr[k]
        mean_cnt /= j-i+1

        # 평균과 같은 원소 있는지 검증
        for k in range(i,j+1) :
            if mean_cnt == arr[k] :
                ans_cnt += 1
                break

print(ans_cnt)