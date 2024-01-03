dx = [1,0,-1,0]
dy = [0,-1,0,1]

n, m = map(int,input().split())

coo = [[0 for i in range(n)] for j in range(n)]

def isPA(x,y) :
    cnt = 0
    for i in range(4) :
        try :
            if coo[x+dx[i]][y+dy[i]] == 1 :
                cnt += 1
        except :
            continue
    if cnt == 3 :
        return 1
    else :
        return 0


for i in range(m) :
    r, c = map(int,input().split())
    coo[r-1][c-1] = 1
    print(isPA(r-1,c-1))