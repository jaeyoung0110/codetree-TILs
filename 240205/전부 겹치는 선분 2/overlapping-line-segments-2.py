# 0 import
import copy

# 1 input, var
n = int(input())
datas = []
for _ in range(n) :
    datas.append(list(map(int,input().split())))

# 2 algorithm
# 완탐으로 하나씩 빼면서 확인
ans = 'No'

for i in range(n) :
    coo = [0 for _ in range(101)]
    if ans == 'Yes' : break
    copy_datas = copy.deepcopy(datas)
    copy_datas.pop(i)
    for data in datas :
        for i in range(data[0],data[1]+1) :
            coo[i] += 1
    for i in coo :
        if i == n-1 :
            ans = 'Yes'
            break

print(ans)