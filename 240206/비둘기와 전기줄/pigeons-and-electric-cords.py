# 0 

# 1 
n = int(input())

# 2
ans_cnt = 0
pigeon_arr = [-1 for _ in range(10)]

for _ in range(n) :
    n, l = map(int,input().split())
    if pigeon_arr[n-1] == -1 :
        pigeon_arr[n-1] = l
        continue
    if pigeon_arr[n-1] != l :
        ans_cnt += 1
        pigeon_arr[n-1] = l

print(ans_cnt)