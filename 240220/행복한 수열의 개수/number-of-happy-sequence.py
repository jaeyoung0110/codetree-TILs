# input
N, M = map(int,input().split())

data_arr = []
for _ in range(N) :
    data_arr.append(list(map(int,input().split())))

# algorithm
ans_cnt = 0

# row
for i in range(N) :
    dup_cnt = 1
    for j in range(N-1) :
        if data_arr[i][j] == data_arr[i][j+1] : dup_cnt += 1
        else : dup_cnt = 1
        if dup_cnt == M :
            ans_cnt += 1
            break
# col
for i in range(N) :
    dup_cnt = 1
    for j in range(N-1) :
        if data_arr[j][i] == data_arr[j+1][i] : dup_cnt += 1
        else : dup_cnt = 1
        if dup_cnt == M :
            ans_cnt += 1
            break
# print
print(ans_cnt)