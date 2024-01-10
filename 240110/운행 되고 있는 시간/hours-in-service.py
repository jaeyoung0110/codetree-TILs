# 입출력 + 초기값 설정
N = int(input())

datas = []
for _ in range(N) :
    datas.append(list(map(int,input().split())))

max_ontime = 0

# 알고리즘
for i in range(N) : # i : 빼는 사람
    coo_time = [0 for i in range(1000)] # 0-999 시간
    sum_ontime = 0
    for j in range(N) : # j : 완전탐색 사람idx
        if j==i : continue
        for k in range(datas[j][0],datas[j][1]) :
            coo_time[k] = 1
    sum_ontime = sum(coo_time)
    max_ontime = max(max_ontime,sum_ontime)

print(max_ontime)