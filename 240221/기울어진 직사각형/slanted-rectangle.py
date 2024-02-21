## input
n = int(input())
data_arr = []
for _ in range(n) :
    data_arr.append(list(map(int,input().split())))

## declaration
# var
ans_max_sum = 0
# function
def is_in_arr(x,y,n) :
    if x in [i for i in range(n)] and y in [i for i in range(n)]: return True
    else : return False



## algorithm
# 완전탐색
for r in range(2,n) :
    for c in range(1,n) : # start (r,c)
        for R in range(1,n-c) :
            for L in range(1,c+1) : # move (R,L)
                if R+L > r : continue
                sub_sum = 0
                for _ in range(R) :
                    r -= 1
                    c += 1
                    sub_sum += data_arr[r][c]
                for _ in range(L) :
                    r -= 1
                    c -= 1
                    sub_sum += data_arr[r][c]
                for _ in range(R) :
                    r += 1
                    c -= 1
                    sub_sum += data_arr[r][c]
                for _ in range(L) :
                    r += 1
                    c += 1
                    sub_sum += data_arr[r][c]
                ans_max_sum = max(ans_max_sum,sub_sum)



## print
print(ans_max_sum)