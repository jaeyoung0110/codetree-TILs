R, C = map(int,input().split())
coo = []
for i in range(R) :
    coo.append(list(input().split()))

color_start = coo[0][0]
ans_cnt = 0

for i in range(1,R-1) :
    for j in range(1,C-1) :
        for ii in range(i+1, R-1) :
            for jj in range(j+1, C-1) :
                if color_start == 'W' :
                    if coo[i][j] == 'B' and coo[ii][jj] == 'W' :
                        ans_cnt += 1
                else :
                    if coo[i][j] == 'W' and coo[ii][jj] == 'B' :
                        ans_cnt += 1

print(ans_cnt)