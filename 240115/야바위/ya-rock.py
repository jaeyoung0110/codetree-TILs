# 1
N = int(input())
datas = []
for _ in range(N) :
    datas.append(list(map(int,input().split())))
ans_max = 0

# 2
for i in range(3) : # 종이컵 위치 idx
    arr = [0, 0, 0]
    arr[i] = 1
    cnt = 0
    for data in datas :
        arr[data[0]-1], arr[data[1]-1] = arr[data[1]-1], arr[data[0]-1]
        if arr[data[2]-1] == 1 :
            cnt += 1
    ans_max = max(ans_max, cnt)

# 3
print(ans_max)