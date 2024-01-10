# import 
import copy

# 서론
N, B = map(int,input().split())
max_cnt = 0
datas_std = []
for _ in range(N) :
    datas_std.append(int(input()))

# 알골
for i in range(N) : # 완탐
    copy_datas = copy.deepcopy(datas_std)
    copy_datas[i] /= 2
    copy_datas = sorted(copy_datas)
    sum_cost = 0
    sum_cnt = 0
    for price in copy_datas :
        sum_cost += price
        if sum_cost > B :
            break
        sum_cnt += 1
    max_cnt = max(max_cnt, sum_cnt)

# print
print(max_cnt)