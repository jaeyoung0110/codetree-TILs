## input
n,t = map(int,input().split())
coo = []
for _ in range(2) :
    coo.append(list(map(int,input().split())))

## declare
def move_belt(coo) :
    tmp = coo[0][n-1]
    for i in range(n-1,0,-1) :
        coo[0][i] = coo[0][i-1]
    coo[0][0] = coo[1][n-1]
    for i in range(n-1,0,-1) :
        coo[1][i] = coo[1][i-1]
    coo[1][0] = tmp

## algorithm
for _ in range(t) :
    move_belt(coo)

## print
for line in coo :
    print(*line)