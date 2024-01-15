# 1
N = int(input())
datas = []
for _ in range(N) :
    datas.append(int(input()))

# 2
ans_cnt = 0
for l in range(1,1001) :
    cnt = 0
    is_on = []
    for v in datas :
        if v >= l : is_on.append(1)
        else : is_on.append(0)
    cng = 2 if is_on[0] == 1 else 1
    for i in range(len(is_on)-1) :
        if is_on[i] != is_on[i+1] :
            cng += 1
    cnt = cng//2
    ans_cnt = max(ans_cnt, cnt)

print(ans_cnt)