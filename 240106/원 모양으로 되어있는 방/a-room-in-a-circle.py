N = int(input())

data_room = []
for i in range(N) :
    data_room.append(int(input()))

min_dis = 0

for start_idx in range(N) :
    cnt = 0
    dis = 0
    for i in range(start_idx,N+start_idx) :
        if i >= N :
            i -=N
        cnt += data_room[i]*dis
        dis += 1
    if start_idx == 1 :
        min_dis = cnt
        continue
    min_dis = min(min_dis,cnt)
print(min_dis)