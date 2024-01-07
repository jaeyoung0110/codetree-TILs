N, M = map(int,input().split())
coo = []
for _ in range(N) :
    row = []
    for i in input() :
        row.append(i)
    coo.append(row)

ans = 0

# -
for r in range(N) :
    for c in range(M-2) :
        if (coo[r][c] == 'L' and coo[r][c+1] == 'E' and coo[r][c+2] == 'E') or (coo[r][c] == 'E' and coo[r][c+1] == 'E' and coo[r][c+2] == 'L') :
            ans += 1
# |
for r in range(N-2) :
    for c in range(M) :
        if (coo[r][c] == 'L' and coo[r+1][c] == 'E' and coo[r+2][c] == 'E') or (coo[r][c] == 'E' and coo[r+1][c] == 'E' and coo[r+2][c] == 'L') :
            ans += 1
# /
for r in range(N-2) :
    for c in range(2,M) :
        if (coo[r][c] == 'L' and coo[r+1][c-1] == 'E' and coo[r+2][c-2] == 'E') or (coo[r][c] == 'E' and coo[r+1][c-1] == 'E' and coo[r+2][c-2] == 'L') :
            ans += 1
# \
for r in range(N-2) :
    for c in range(M-2) :
        if (coo[r][c] == 'L' and coo[r+1][c+1] == 'E' and coo[r+2][c+2] == 'E') or (coo[r][c] == 'E' and coo[r+1][c+1] == 'E' and coo[r+2][c+2] == 'L') :
            ans += 1

print(ans)