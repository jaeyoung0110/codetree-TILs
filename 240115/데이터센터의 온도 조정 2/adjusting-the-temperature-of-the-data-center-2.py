# input , var
N, C, G, H = map(int,input().split())
datas_tmp = []
for _ in range(N) :
    datas_tmp.append(list(map(int,input().split())))

ans_max = 0

# algorithm

def work(t,data) :
    if t < data[0] :
        return C
    elif t > data[1] :
        return H
    else :
        return G

for t in range(1000) :
    sum_work = 0
    for i in range(N) :
        sum_work += work(t, datas_tmp[i])
    ans_max = max(ans_max, sum_work)

print(ans_max)