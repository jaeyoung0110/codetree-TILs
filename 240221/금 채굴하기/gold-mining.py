# input
n, m = map(int,input().split())
data_arr = []
for _ in range(n) :
    data_arr.append(list(map(int,input().split())))

# algorithm
def is_range(x,y) :
    if x in [i for i in range(n)] and y in [i for i in range(n)] : return True
    else : return False

def is_rhom(k,i,j,x,y) :
    if abs(x-i) + abs(y-j) <= k : return True
    else : return False

ans_max_gold = 0
for k in range(n+1) :
    for i in range(n) :
        for j in range(n) :
            gold_value = 0
            gold_cnt = 0
            for x in range(n) :
                for y in range(n) :
                    if is_range(x,y) and is_rhom(k,i,j,x,y) :
                        if data_arr[x][y] == 1 :
                            gold_value += m
                            gold_cnt += 1
            if gold_value >= (k*k) + (k+1)*(k+1) :
                ans_max_gold = max(ans_max_gold,gold_cnt)

# print
print(ans_max_gold)