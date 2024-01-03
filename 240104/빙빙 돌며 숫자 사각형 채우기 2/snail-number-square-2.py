n, m = map(int,input().split())

coo = [[0 for _ in range(m*2)] for _ in range(n*2)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
state = [0,0,1]

for i in range(1,n*m+1) :
    coo[state[1]][state[0]] = i
    state[0] = state[0] + dx[state[2]]
    state[1] = state[1] + dy[state[2]]
    if not((0 <= state[0] < m) and (0 <= state[1] < n) and (coo[state[1]][state[0]] == 0)) :
        state[0] = state[0] - dx[state[2]]
        state[1] = state[1] - dy[state[2]] 
        state[2] = (state[2]-1)%4
        state[0] = state[0] + dx[state[2]]
        state[1] = state[1] + dy[state[2]]

for i in range(n) :
    for j in range(m) :
        print(coo[i][j], end = ' ')
    print()