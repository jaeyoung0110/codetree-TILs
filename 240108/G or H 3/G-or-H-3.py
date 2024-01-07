N, K = map(int,input().split())

data = []
for i in range(N) :
    data.append(list(input().split()))

# 위치중 최댓값 찾기
max_idx = 0
for i in data :
    max_idx = max(max_idx, int(i[0]))

# 최대 길이만큼 좌표 만들기
coo = [0 for i in range(max_idx)]

# 좌표에 데이터 등록
for i in data :
    coo[int(i[0])-1] = i[1]

max_sum = 0

if K > len(coo) :
    for i in data :
        max_sum += i[1]

for i in range(len(coo) - K) :
    sum_data = 0
    for j in range(i, i+K+1) :
        if coo[j] == 'G' :
            sum_data += 1
        elif coo[j] == 'H' :
            sum_data += 2
    max_sum = max(max_sum, sum_data)

print(max_sum)