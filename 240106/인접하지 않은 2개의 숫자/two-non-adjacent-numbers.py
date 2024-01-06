n = int(input())
datas = list(map(int,input().split()))

ans_max = 0

for i in range(n) :
    for j in range(i+2,n) :
        ans_max = max(ans_max, datas[i]+datas[j])

print(ans_max)