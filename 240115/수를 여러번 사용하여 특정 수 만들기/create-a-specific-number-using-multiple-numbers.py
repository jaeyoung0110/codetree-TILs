# 1
A, B, C = map(int,input().split())
ans_max = 0

# 2 
for i in range(1000) :
    for j in range(1000) :
        if A*i + B*j > C : continue
        else :
            ans_max = max(ans_max, A*i + B*j)

# 3
print(ans_max)