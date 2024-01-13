#import
import copy

# 입력부
N, B = map(int,input().split())
datas = []
for _ in range(N) :
    datas.append(list(map(int,input().split())))

ans_max = 0

for i in range(N) :
    c_datas = copy.deepcopy(datas)
    c_datas[i][0] /= 2
    for j in range(N) :
        c_datas[j] = c_datas[j][0] + c_datas[j][1]
    c_datas.sort()
    max_cnt = 0
    sum_price = 0
    for j in range(N) :
        if sum_price + c_datas[j] > B :
            break
        sum_price += c_datas[j]
        max_cnt += 1
    ans_max = max(ans_max, max_cnt)

print(ans_max)