n = int(input())

coo = [[0 for _ in range(n)] for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
state = [n//2,n//2,0]

# print('x,y : ',state[0],state[1])
for i in range(1,n*n+1) :
    coo[state[1]][state[0]] = i
    if i == 1 :
        state[0] = state[0] + dx[state[2]]
        state[1] = state[1] + dy[state[2]]
        # print('x,y : ',state[0],state[1])
        continue
    if (coo[state[1]+dy[(state[2]-1)%4]][state[0]+dx[(state[2]-1)%4]] == 0) :
        state[2] = (state[2]-1)%4
        state[0] = state[0] + dx[state[2]]
        state[1] = state[1] + dy[state[2]]
    else :
        state[0] = state[0] + dx[state[2]]
        state[1] = state[1] + dy[state[2]]
    # print('x,y : ',state[0],state[1])

for i in range(n) :
    for j in range(n) :
        print(coo[i][j], end = ' ')
    print()