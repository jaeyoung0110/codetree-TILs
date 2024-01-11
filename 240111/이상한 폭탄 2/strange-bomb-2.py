N, K = map(int,input().split())
coo = []
for _ in range(N) :
    coo.append(int(input()))
ans_num = -1

for i in range(1001) :
    boom_idx = []
    for idx, data in enumerate(coo) :
        if data == i :
            boom_idx.append(idx)
    for j in range(len(boom_idx)-1) :
        if abs(boom_idx[j] - boom_idx[j+1]) <= K :
            ans_num = max(ans_num, i)

print(ans_num)