# input
n,m = map(int,input().split())
data_arr = []
for _ in range(n) :
    data_arr.append(list(map(int,input().split())))

# algorithm 
ans_max = 0
# ㄱ자
for i in range(n-1) :
    for j in range(m-1) :
        ans_max = max(ans_max,(data_arr[i][j] + data_arr[i+1][j] + data_arr[i][j+1]), (data_arr[i][j] + data_arr[i][j+1] + data_arr[i+1][j+1]),(data_arr[i][j+1] + data_arr[i+1][j+1] + data_arr[i+1][j]),(data_arr[i][j] + data_arr[i+1][j] + data_arr[i+1][j+1]))

# -자
for i in range(n) : 
    for j in range(m-2) :
        ans_max = max(ans_max,(data_arr[i][j] + data_arr[i][j+1] + data_arr[i][j+2]))

# ㅣ자
for i in range(n-2) :
    for j in range(m) :
        ans_max = max(ans_max, (data_arr[i][j] + data_arr[i+1][j] + data_arr[i+2][j]))

# print
print(ans_max)