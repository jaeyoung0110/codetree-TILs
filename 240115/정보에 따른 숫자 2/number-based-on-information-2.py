# input / var
T, a, b = map(int,input().split())
datas = []
coo = [0 for _ in range(b+1)]
for _ in range(T) :
    c, x = input().split()
    x = int(x)
    datas.append([c,x])
    coo[x] = c

ans_cnt = 0

# algorithm
for i in range(a,b+1) :
    min_s, min_n = 1000, 1000
    for j,v in enumerate(coo) :
        if v == 0 : continue
        if v == 'S' :
            min_s = min(min_s,abs(j - i))
        elif v == 'N' :
            min_n = min(min_n,abs(j - i))
    if min_s <= min_n :
        ans_cnt += 1

# print
print(ans_cnt)