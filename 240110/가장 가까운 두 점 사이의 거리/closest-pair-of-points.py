# import
import sys

# 입력부 처리
N = int(input())
datas = []
for _ in range(N) :
    datas.append(list(map(int,input().split())))

# 출력부 처리
ans_min_sq = sys.maxsize

# 알고리즘
for i in range(N) :
    for j in range(i+1,N) :
        dis_sq = abs(datas[i][0]-datas[j][0])**2 + abs(datas[i][1] - datas[j][1])**2
        ans_min_sq = min(ans_min_sq,dis_sq)

print(ans_min_sq)