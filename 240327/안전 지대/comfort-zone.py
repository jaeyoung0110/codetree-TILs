## k값에 따라 그리드DFS 해서 덩어리 개수 구함
## 최댓값 갱신 + 최댓값에 k도 같이 저장
ans = [0,1]

N, M = map(int,input().split())
grid = []
for _ in range(N) :
    grid.append(list(map(int,input().split())))

def is_range(r,c) :
    if r >= 0 and r < N and c >= 0 and c < M :
        return True
    return False

def dfs(vertex_r,vertex_c, visited, k) :
    mr = [-1,0,1,0]
    mc = [0,1,0,-1]
    visited[vertex_r][vertex_c] = True
    for dr, dc in zip(mr,mc) : 
        if is_range(vertex_r+dr,vertex_c+dc) and grid[vertex_r+dr][vertex_c+dc] > k and not visited[vertex_r+dr][vertex_c+dc] :
            visited[vertex_r+dr][vertex_c+dc] = True
            dfs(vertex_r+dr,vertex_c+dc,visited,k)


for k in range(1,101) :
    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt_city = 0
    for r in range(N) :
        for c in range(M) :
            if grid[r][c] > k and not visited[r][c]:
                cnt_city += 1
                dfs(r,c,visited,k)
    if ans[0] < cnt_city :
        ans[0] = cnt_city
        ans[1] = k

print(ans[1],ans[0])