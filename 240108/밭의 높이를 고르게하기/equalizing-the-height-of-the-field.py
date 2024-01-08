N, H, T = map(int,input().split())
coo = list(map(int,input().split()))

# 구간길이 T 로 완전탐색 해서 각 경우마다 비용 계산 최솟값으로
min_cost = 0

for i in range(N-T+1) :
    sum_cost = 0
    for j in range(i,T+i) : # 인덱스 I 부터 구간 길이 T 만큼
        sum_cost += abs(coo[j] - H)
    if i == 0 :
        min_cost = sum_cost
    else :
        min_cost = min(min_cost, sum_cost)

print(min_cost)