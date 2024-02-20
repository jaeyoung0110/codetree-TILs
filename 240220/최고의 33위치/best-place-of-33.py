# 1
N = int(input())
coo = []
for _ in range(N) :
    coo.append(list(map(int,input().split())))

ans = 0

for i in range(N-2) :
    for j in range(N-2) :
        cnt = 0
        # i, j is start idx
        for x in range(i,i+3) :
            for y in range(j, j+3) :
                cnt += coo[x][y]

        ans = max(ans,cnt)

print(ans)

# n^2