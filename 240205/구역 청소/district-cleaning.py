coo = [0 for _ in range(100)]

data_A = list(map(int,input().split()))
data_B = list(map(int,input().split()))

for i in range(data_A[0],data_A[1]) :
    coo[i] = 1
for i in range(data_B[0],data_B[1]) :
    coo[i] = 1

ans_cnt = 0
for i in coo :
    if i == 1 :
        ans_cnt += 1


print(ans_cnt)