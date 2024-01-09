datas = list(map(int,input().split()))

min_diff = -1

for t1 in range(5) :
    for t21 in range(5) :
        if t21 == t1 : continue
        for t22 in range(t21+1, 5) :
            if t21 == t1 : continue
            sum1 = datas[t1]
            sum2 = datas[t21] + datas[t22]
            sum3 = sum(datas) - (sum1 + sum2)
            if sum1 == sum2 or sum1 == sum3 or sum2 == sum3 :
                continue
            sum_diff = max(sum1,sum2,sum3) - min(sum1,sum2,sum3)
            if min_diff == -1 :
                min_diff = sum_diff
            else :
                min_diff = min(min_diff, sum_diff)

print(min_diff)