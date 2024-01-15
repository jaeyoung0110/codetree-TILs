# input, var declare
X, Y = map(int,input().split())

ans_cnt = 0

# algorithm
def inter(i) :
    arr = [0 for _ in range(10)]
    for v in str(i) :
        arr[int(v)] += 1
    x, y = 0, 0
    for k in arr :
        if k != 0 :
            if k == 1 :
                x += 1
            y += 1
    if x == 1 and y == 2 :
        return True
    else :
        return False


for i in range(X,Y+1) :
    if inter(i) == True :
        ans_cnt += 1

# print
print(ans_cnt)