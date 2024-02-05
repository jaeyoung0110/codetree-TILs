coo = [0 for _ in range(100)]

n = int(input())

datas = []
for _ in range(n) :
    datas.append(list(map(int,input().split())))

for data in datas :
    for i in range(data[0], data[1]+1) :
        coo[i] += 1
    
ans = 'No'

for i in coo :
    if i == n :
        ans = "Yes" 
        break

print(ans)