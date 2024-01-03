# 입력값 할당
N, T = map(int,input().split())
S = input()

# 좌표평면 생성
coo = []
for _ in range(N) :
    coo.append(list(map(int,input().split())))

dx, dy = [1,0,-1,0], [0,1,0,-1] # 동서남북
state = [N//2,N//2,3] # [x좌표,y좌표,방향]
total = coo[state[1]][state[0]]

# print("x,y : ",state[0],state[1])
for s in S :
    if s == 'R' :
        state[2] = (state[2]+1)%4
        # print("dir changed : ",state[2])
    elif s == 'L' :
        state[2] = (state[2]-1)%4
        # print("dir changed : ",state[2])
    elif s == 'F' :
        state[0] = state[0] + dx[state[2]]
        state[1] = state[1] + dy[state[2]]
        if not(0 <= state[0] < N and 0 <= state[1] < N) :
            state[0] = state[0] - dx[state[2]]
            state[1] = state[1] - dy[state[2]]
            continue
            # print("ignored command")
        total += coo[state[1]][state[0]]
        # print("x,y changed : ",state[0],state[1])

print(total)