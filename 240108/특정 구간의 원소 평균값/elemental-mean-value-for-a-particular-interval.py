N = int(input())
arr = list(map(int,input().split()))

ans_cnt = 0

for i in range(N) :
    for j in range(i, N) :
        if i == j :
            ans_cnt += 1
            continue
        mean_cnt = 0
        for k in range(i,j+1) :
            mean_cnt += arr[k]
        mean_cnt /= j-i
        for k in range(i,j+1) :
            if mean_cnt == arr[k] :
                ans_cnt += 1
                break

print(ans_cnt)