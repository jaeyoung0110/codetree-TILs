# 1
X, Y = map(int,input().split())
ans_cnt = 0

# 2
for i in range(X,Y+1) :
    i = str(i)
    is_p = True
    for j in range(len(i)//2) :
        if i[j] != i[-(j+1)] :
            is_p = False
    if is_p == True :
        ans_cnt += 1

# 3
print(ans_cnt)