import copy

N = int(input())

data_coo = []
for i in range(N) :
    data_coo.append(list(map(int,input().split())))

min_dis = 99999

for j in range(1,N-1) :
    copy_coo = copy.deepcopy(data_coo)
    copy_coo.pop(j)
    dis = 0
    for i in range(N-2) :
        dis += (abs(copy_coo[i+1][0]-copy_coo[i][0])+abs(copy_coo[i+1][1]-copy_coo[i][1]))
    min_dis = min(min_dis,dis)

print(min_dis)