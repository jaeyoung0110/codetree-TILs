N = int(input())
coo = []

for _ in range(N) :
    data = input()
    coo.append(data)

k = int(input())

state = [0,0,'d']

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def start(k) :
    if k//N == 0 :
        state[0] = k-1
        state[1] = 0
        state[2] = 1
    elif k//N == 1 :
        state[0] = N-1
        state[1] = (k-N)-1
        state[2] = 2
    elif k//N == 2 :
        state[0] = N-(k-N*2)
        state[1] = N-1
        state[2] = 3
    elif k//N == 3 :
        state[0] = 0
        state[1] = N-(k-N*3)
        state[2] = 0

def bs(state, d) :
    if d == '/' :
        if state[2] == 0 :
            state[2] = 3
        elif state[2] == 1 :
            state[2] = 2
        elif state[2] == 2 :
            state[2] = 1
        elif state[2] == 3 :
            state[2] = 0
    elif d == '\\' :
        if state[2] == 0 :
            state[2] = 1
        elif state[2] == 1 :
            state[2] = 0
        elif state[2] == 2 :
            state[2] = 3
        elif state[2] == 3 :
            state[2] = 2
    state[0] = state[0]+dx[state[2]]
    state[1] = state[1]+dy[state[2]]

start(k)

cnt = 0
# print('현재 좌표 : ',state[0],state[1])
while 0 <= state[0] < N and 0<= state[1] < N :
    bs(state,coo[state[1]][state[0]])
    # print('현재 좌표 : ',state[0],state[1])
    cnt += 1

print(cnt)