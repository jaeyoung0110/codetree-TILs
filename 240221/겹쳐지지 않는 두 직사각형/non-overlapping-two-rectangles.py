# import
import sys

# input
n,m = map(int,input().split())
coo = []
for _ in range(n) :
    coo.append(list(map(int,input().split())))

## declare
# var
ans_max_sum = -sys.maxsize
# fun
def is_dup(r1,c1,y1,x1,r2,c2,y2,x2) :
    for y in range(r1, r1+y1) :
        for x in range(c1, c1+x1) :
            if (y >= r2 and y <= r2+y2-1) and (x >= c2 and x <= c2+x2-1) : return False
    return True

## algorithm
# 첫 사각형 선택
for r1 in range(n) :
    for c1 in range(m) : # start : (r1,c1)
        for y1 in range(1, n+1 - r1) :
            for x1 in range(1, m+1 - c1) : # length : (y1,x1)

                for r2 in range(n) :
                    for c2 in range(m) :
                        for y2 in range(1, n+1 - r2) :
                            for x2 in range(1, m+1 - c2) :
                                sub_sum = 0
                                if is_dup(r1,c1,y1,x1,r2,c2,y2,x2) :
                                    for i in range(r1,r1+y1) :
                                        for j in range(c1,c1+x1) :
                                            sub_sum += coo[i][j]
                                    for i in range(r2,r2+y2) :
                                        for j in range(c2,c2+x2) :
                                            sub_sum += coo[i][j]
                                    ans_max_sum = max(ans_max_sum,sub_sum)


        
# 두번째 사각형 선택

# print
print(ans_max_sum)