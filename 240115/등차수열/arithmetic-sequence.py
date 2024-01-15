# input / var
n = int(input())
nums = list(map(int,input().split()))
ans_cnt = 0

# algorithm
for k in range(2, 100) :
    cnt = 0
    for i in range(n) :
        for j in range(i+1, n) :
            if nums[i] - k == k - nums[j] :
                cnt += 1
    ans_cnt = max(ans_cnt, cnt)

# print
print(ans_cnt)