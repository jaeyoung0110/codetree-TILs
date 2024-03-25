n,m = map(int,input().split())

grid = []
for _ in range(n) :
    grid.append(list(map(int,input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]

ans_poss = False

def dfs(r,c) : # 0 사용 # 시작 방문 / 연결 경로 포문 - 갈수 있고, 안간 곳 비짓넣고 dfs
    global ans_poss
    if r+1 == n and c+1 == m :
        ans_poss = True
        return 
    visited[r][c] = True

    if r+1 < n and grid[r+1][c] == 1 and not visited[r+1][c] :
        visited[r+1][c] = True
        dfs(r+1,c)
    if c+1 < m and grid[r][c+1] == 1 and not visited[r][c+1] :
        visited[r][c+1] = True
        dfs(r,c+1)

dfs(0,0)

if ans_poss :
    print(1)
else :
    print(0)