import itertools as it

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
beatuty = []

for i in it.permutations(B,len(B)) :
    beatuty.append(list((i)))

ans_cnt = 0

for i in range(N-M+1) :
    sub_arr = []
    for j in range(i, i+M) :
        sub_arr.append(A[j])
    if sub_arr in beatuty :
        ans_cnt += 1

print(ans_cnt)