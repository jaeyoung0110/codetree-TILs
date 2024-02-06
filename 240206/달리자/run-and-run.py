# 1
n = int(input())
data_A = list(map(int,input().split()))
data_B = list(map(int,input().split()))

# 2
ans_cnt = 0

for i in range(n) :
    ans_cnt += (data_A[i] - data_B[i])
    if i < n-1 :
        data_A[i+1] += data_A[i] - data_B[i]

print(ans_cnt)