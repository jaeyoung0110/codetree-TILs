N, M = map(int,input().split())
links = []
for _ in range(M) :
    links.append(list(map(int,input().split())))

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for link in links :
    graph[link[0]][link[1]] = 1
    graph[link[1]][link[0]] = 1

visited = [False for _ in range(N+1)]

def dfs(vertex,graph,visited) :
    visited[vertex] = True
    for i, v in enumerate(graph[vertex]) :
        if v and not visited[i] :
            visited[i] = True
            dfs(i,graph,visited)
    
dfs(1,graph,visited)
print(visited.count(True)-1)