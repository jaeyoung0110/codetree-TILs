datas = list(map(int,input().split()))

min_diff = 2000000

for t1_1 in range(6) :
    for t1_2 in range(t1_1+1, 6) :
        for t2_1 in range(6) :
            if t2_1 == t1_1 or t2_1 == t1_2 : 
                continue
            for t2_2 in range(t2_1+1, 6) :
                if t2_2 == t1_1 or t2_2 == t1_2 : 
                    continue
                sum_t1 = datas[t1_1] + datas[t1_2]
                sum_t2 = datas[t2_1] + datas[t2_2]
                sum_t3 = sum(datas) - (sum_t1 + sum_t2)
                sum_diff = max(sum_t1,sum_t2,sum_t3) - min(sum_t1,sum_t2,sum_t3)
                min_diff = min(min_diff,sum_diff)

print(min_diff)