n, m = map(int,input().split())

coo = [[0 for _ in range(m)] for _ in range(n)]

state = {'x':0, 'y':0, 'd':0}
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n*m) :
    alp = chr(i%26+65)
    coo[state['y']][state['x']] = alp
    state['x'] = state['x'] + dx[state['d']]
    state['y'] = state['y'] + dy[state['d']]
    if not((0 <= state['x'] < m) and (0 <= state['y'] < n) and (coo[state['y']][state['x']] == 0)) :
        state['x'] = state['x'] - dx[state['d']]
        state['y'] = state['y'] - dy[state['d']] 
        state['d'] = (state['d']+1)%4
        state['x'] = state['x'] + dx[state['d']]
        state['y'] = state['y'] + dy[state['d']]

for i in range(n) :
    for j in range(m) :
        print(coo[i][j], end=' ')
    print()