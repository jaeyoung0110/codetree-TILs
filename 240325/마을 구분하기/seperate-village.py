n = int(input())
grid = []
for _ in range(n) :
    grid.append(list(map(int,input().split())))

visited = [[False for _ in range(n)] for _ in range(n)]

def dfs(r,c) :
    def is_range(r,c) :
        if 0<=r and r<n and 0<=c and c<n : return True
        else : return False
    global people_cnt
    visited[r][c] = True
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    for mr, mc in zip(dr,dc) :
        if is_range(r+mr,c+mc) and grid[r+mr][c+mc] == 1 and not visited[r+mr][c+mc] :
            visited[r+mr][c+mc] = True
            people_cnt += 1
            dfs(r+mr,c+mc)


arr_people_cnt = []

for r in range(n) :
    for c in range(n) :
        if grid[r][c] == 1 and not visited[r][c] :
            people_cnt = 1
            dfs(r,c)
            arr_people_cnt.append(people_cnt)



arr_people_cnt.sort()
print(len(arr_people_cnt))
for data in arr_people_cnt :
    print(data)