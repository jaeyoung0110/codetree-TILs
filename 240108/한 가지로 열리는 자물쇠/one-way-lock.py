N = int(input())
data = list(map(int,input().split()))

# 완전탐색 
ans_cnt = 0

for i in range(1,N+1) :
    for j in range(1,N+1) :
        for k in range(1,N+1) :
            if abs(i-data[0])<=2 or abs(j-data[1])<=2 or abs(k-data[2])<=2 :
                ans_cnt += 1

print(ans_cnt)