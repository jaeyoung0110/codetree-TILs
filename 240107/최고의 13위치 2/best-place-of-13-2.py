N = int(input())
coo = []
for _ in range(N) :
    coo.append(list(map(int,input().split())))

max_cnt = 0

for i in range(N) :
    for j in range(N-2) :
        for ii in range(N) :
            for jj in range(N-2) :
                # i,j / ii,jj / 겹치면 패스
                if ii == i and abs(jj-j) <= 2 :
                    continue
                # 개수 최대 판단
                max_cnt = max(max_cnt, coo[i][j]+coo[i][j+1]+coo[i][j+2]+coo[ii][jj]+coo[ii][jj+1]+coo[ii][jj+2])

print(max_cnt)