## input
n, m = map(int,input().split())
coo = []
for _ in range(n) :
    coo.append(list(map(int,input().split())))

## declare
# var
ans_max_size = -1
# fuc
def is_plus_square(r,c,h,l) :
    for y in range(r,r+h) :
        for x in range(c,c+l) :
            if coo[y][x] <= 0 : return False
    return True

## algotithm
#1 사각형 선택 
for r in range(n) : 
    for c in range(m) :
        for h in range(1,n-r+1) :
            for l in range(1,m-c+1) :
                #2 사각형 탐색 및 양수사각형 확인
                if is_plus_square(r,c,h,l) :
                    ans_max_size = max(ans_max_size,h*l)


## print
print(ans_max_size)