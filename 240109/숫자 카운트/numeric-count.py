def guess(pred, data) : # int형으로 받음
    cnt_1, cnt_2 = 0, 0
    pred, data = str(pred), str(data)
    for i,v in enumerate(data) :
        if v in  :
            if pred[i] == v :
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
            if i == j or i == k or j == k :
                continue
            same_cnt = 0
            ans = i*100+j*10+k
            for l in range(N) :
                if guess(ans,data[l][0]) == [data[l][1],data[l][2]] :
                    same_cnt += 1
            if same_cnt == N :
                ans_cnt += 1

print(ans_cnt)