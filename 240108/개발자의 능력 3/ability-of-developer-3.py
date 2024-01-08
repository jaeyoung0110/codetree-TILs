data = list(map(int,input().split()))

def get_diff(i,j,k) :
    sum_1 = data[i] + data[j] + data[k]
    sum_2 = sum(data) - sum_1
    return abs(sum_2 - sum_1)

ans_diff = 0

# 사람 인덱스 기준 완전탐색
for i in range(6) :
    for j in range(i+1,6) :
        for k in range(j+1,6) :
            if i==0 and j==1 and k==2 :
                ans_diff = get_diff(i,j,k)
            else :
                ans_diff = min(ans_diff, get_diff(i,j,k))

print(ans_diff)