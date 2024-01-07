import sys

N, S = map(int,input().split())
data = list(map(int,input().split()))

gap = sys.maxsize

for i in range(N) :
    for j in range(i+1, N) :
        sum_int = 0
        for k in range(N) :
            if k == i or k == j :
                continue
            sum_int += data[k]
        gap = min(gap,abs(sum_int-S))


print(gap)