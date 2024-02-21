## import


## input
n, t = map(int,input().split())
data_belt = []
for _ in range(3) :
    data_belt.append(list(map(int,input().split())))

## declare
def move_belt(data_belt) :
    tmp = data_belt[0][n-1]
    for i in range(n-1,0,-1) :
        data_belt[0][i] = data_belt[0][i-1]
    data_belt[0][0] = data_belt[2][n-1]
    for i in range(n-1,0,-1) :
        data_belt[2][i] = data_belt[2][i-1]
    data_belt[2][0] = data_belt[1][n-1]
    for i in range(n-1,0,-1) :
        data_belt[1][i] = data_belt[1][i-1]
    data_belt[1][0] = tmp

## algorithm
for _ in range(t) :
    move_belt(data_belt)

## print
for line in data_belt :
    print(*line)