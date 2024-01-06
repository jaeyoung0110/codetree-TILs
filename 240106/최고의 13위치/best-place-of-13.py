N = int(input())
coo = []
for i in range(N) :
    coo.append(list(map(int,input().split())))

max_cnt = 0

for i in range(N) :
    for j in range(N-2) :
        max_cnt = max(max_cnt, coo[i][j] + coo[i][j+1] + coo[i][j+2])

print(max_cnt)