coo = []
for _ in range(19) :
    coo.append(list(map(int,input().split())))

# 가로
def x() :
    for r in range(19) :
        for c in range(19-4) :
            if coo[r][c] != 0 :
                if coo[r][c] == coo[r][c+1] == coo[r][c+2] == coo[r][c+3] == coo[r][c+4] :
                    return coo[r][c], r, c+2 # 색, 행, 열
    # 세로
    for r in range(19-4) :
        for c in range(19) :
            if coo[r][c] != 0 :
                if coo[r][c] == coo[r+1][c] == coo[r+2][c] == coo[r+3][c] == coo[r+4][c] :
                    return coo[r][c], r+2, c # 색, 행, 열
    # \
    for r in range(19-4) :
        for c in range(19-4) :
            if coo[r][c] != 0 :
                if coo[r][c] == coo[r+1][c+1] == coo[r+2][c+2] == coo[r+3][c+3] == coo[r+4][c+4] :
                    return coo[r][c], r+2, c+2 # 색, 행, 열
    # /
    for r in range(4, 19) :
        for c in range(19-4) :
            if coo[r][c] != 0 :
                if coo[r][c] == coo[r-1][c+1] == coo[r-2][c+2] == coo[r-3][c+3] == coo[r-4][c+4] :
                    return coo[r][c], r-2, c+2 # 색, 행, 열
    return False, False, False

ans = x()

if ans[0] == False :
    print(0)
else :
    print(ans[0])
    print(ans[1]+1,ans[2]+1)