# 1
N = int(input())
dots = []
for _ in range(N) :
    dots.append(list(map(int,input().split())))
ans_min = 100

# 2
for i in range(2,101,2) :
    for j in range(2,101,2) :
        quad = [0,0,0,0]
        for dot in dots :
            if dot[0] > i and dot[1] > j : quad[0] += 1
            elif dot[0] > i and dot[1] < j : quad[1] += 1
            elif dot[0] < i and dot[1] < j : quad[2] += 1
            else : quad[3] += 1
        ans_min = min(ans_min, max(quad))

# 3
print(ans_min)