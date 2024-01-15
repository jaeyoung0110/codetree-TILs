# 0 
import sys

# 1
n = int(input())
nums = list(map(int,input().split()))
ans_min = sys.maxsize

# 2
for i in range(n) : # 2배
    nums[i] *= 2
    for j in range(n) : # 제거
        sub_nums = []
        sum_diff = 0
        for k in range(n) :
            if k != j : sub_nums.append(nums[k])
        for k in range(n-2) :
            sum_diff += abs(sub_nums[k] - sub_nums[k+1])
        ans_min = min(ans_min, sum_diff)
    nums[i] //= 2

# 3
print(ans_min)