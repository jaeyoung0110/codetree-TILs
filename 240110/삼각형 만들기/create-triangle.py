# 축에 평행한 삼각형 조건
# 넓이 구하기
# 최댓값 찾기

# 입력부 출력부 변수
N = int(input())
dots = []
ans_max = 0
for _ in range(N) :
    dots.append(list(map(int,input().split())))

# 알고리즘

for i in range(N) :
    for j in range(i+1,N) :
        for k in range(j+1,N) :
            # 삼각형 & 축 평행 
            if (dots[i][0] == dots[j][0] and dots[i][0] == dots[k][0]) \
            or (dots[i][0] != dots[j][0] and dots[i][0] != dots[k][0] and dots[j][0] != dots[k][0]) \
            or (dots[i][1] == dots[j][1] and dots[i][1] == dots[k][1]) \
            or (dots[i][1] != dots[j][1] and dots[i][1] != dots[k][1] and dots[j][1] != dots[k][1]):
                continue
            else :
                ans_max = max(ans_max, (max(dots[i][0],dots[j][0],dots[k][0])-min(dots[i][0],dots[j][0],dots[k][0]))*(max(dots[i][1],dots[j][1],dots[k][1])-min(dots[i][1],dots[j][1],dots[k][1])))

print(ans_max)