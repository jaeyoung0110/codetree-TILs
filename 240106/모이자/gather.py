n = int(input())
arr = list(map(int,input().split()))

minDis = 0

for i in range(n) :
    idx = i
    total = 0
    for j in range(n) :
        total += abs(j-i)*arr[j]
    if i == 1 :
        minDis = total
        continue
    if total < minDis :
        minDis = total

print(minDis)