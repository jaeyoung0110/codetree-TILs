N = int(input())
line = []
for _ in range(N) :
    line.append(list(map(int,input().split())))

ans_cnt = 0

for i in range(N) :
    for j in range(i+1,N) :
        for k in range(j+1,N) :
            coo = [0 for i in range(101)]
            for idx, data in enumerate(line) :
                if idx in [i,j,k] :
                    continue
                for l in range(data[0],data[1]+1) :
                    coo[l] += 1
            is_ok = True
            for data in coo :
                if data > 1 :
                    is_ok = False
            if is_ok == True :
                ans_cnt += 1

print(ans_cnt)