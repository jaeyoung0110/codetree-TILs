MAX_COO_LEN = 100
N, K = map(int,input().split())
coo = [0 for _ in range(MAX_COO_LEN + 1)]

# 좌표에 정보 등록
for i in range(N) :
    cnt, loc = map(int,input().split())
    coo[loc] += cnt
# 범위만큼 세서 최댓값 찾기
ans_cnt = 0
def isRange(K, MAX_COO_LEN) :
    return False if 2*K >= 100 else True

if isRange(K,MAX_COO_LEN) :
    # 센터중심 부분합 구하기
    for center in range(K, len(coo)-K) :# 10 - 90 
        sum_cnt = 0
        for i in range(center-K, center+K+1) :
            sum_cnt += coo[i]
        ans_cnt = max(ans_cnt, sum_cnt)

else :
    for i in range(len(coo)) :
        ans_cnt += coo[i]

print(ans_cnt)