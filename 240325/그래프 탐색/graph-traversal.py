### 1
N, M = map(int,input().split())
DFS = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M) :
    x,y = map(int,input().split())
    DFS[x-1][y-1] = 1
    DFS[y-1][x-1] = 1

### 2
visited = [False for _ in range(N)]

# # stack : push/pop/empty/size/top
# class stack :
#     def __init__(self) :
#         self.stack = []
    
#     def push(self,item) :
#         self.stack.append(item)

vertex_cnt = 0

start_idx = -1
def dfs(idx) :
    global start_idx
    global vertex_cnt
    if start_idx == -1 :
        start_idx = idx
    visited[idx-1] = True

    for i, c in enumerate(DFS[idx-1]) :
        if c == 1 and visited[i] == False :
            visited[i] = True
            vertex_cnt += 1
            dfs(c+1)



### 3
dfs(1)

print(vertex_cnt)