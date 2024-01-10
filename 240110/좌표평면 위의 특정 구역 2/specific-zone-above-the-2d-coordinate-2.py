N = int(input())
datas = []

for _ in range(N) :
    datas.append(list(map(int,input().split())))

ans_min = 1600000000

for i in range(N) : # i = 제거해볼 인덱스
    x_M, x_m = 0, 40000
    y_M, y_m = 0, 40000
    for j in range(N) :
        if j == i : continue
        x_M = max(x_M,datas[j][0])
        x_m = min(x_m,datas[j][0])
        y_M = max(y_M,datas[j][1])
        y_m = min(y_m,datas[j][1])
    area = (x_M - x_m) * (y_M - y_m)
    ans_min = min(ans_min, area)

print(ans_min)