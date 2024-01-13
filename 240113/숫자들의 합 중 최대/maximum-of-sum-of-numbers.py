X, Y = map(int,input().split())

ans_max = 0

for i in range(X,Y+1) :
    sum_max = sum(list(map(int,list(str(i)))))
    ans_max = max(ans_max,sum_max)

print(ans_max)