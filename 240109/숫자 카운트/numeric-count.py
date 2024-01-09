def guess(ans, pred) : # int형으로 받음
    cnt_1, cnt_2 = 0, 0
    ans, pred = str(ans), str(pred)
    for i,v in enumerate(pred) :
        if v in ans :
            if ans[i] == v :
                cnt_1 += 1
            else :
                cnt_2 += 1
    return [cnt_1, cnt_2]

N = int(input())
data = []
for _ in range(N) :
    data.append(list(map(int,input().split())))

ans_cnt = 0

for i in range(1,10) :
    for j in range(1,10) :
        for k in range(1,10) :
            same_cnt = 0
            pred = i*100+j*10+k
            for l in range(N) :
                if guess(data[l][0],pred) == [data[l][1],data[l][2]] :
                    same_cnt += 1
            if same_cnt == N :
                ans_cnt += 1

print(ans_cnt)