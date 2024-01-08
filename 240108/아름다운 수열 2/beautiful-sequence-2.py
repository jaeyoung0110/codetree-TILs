import itertools as it
import copy

N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans_cnt = 0

for i in range(N-M+1) :
    # M 길이의 부분 수열 만들기
    sub_arr = []
    for j in range(i, i+M) :
        sub_arr.append(A[j])
    # 부분 수열의 값이 모두 B와 같이 있는지 - 순서 상관 없음
    equal_cnt = 0
    B_copy = copy.deepcopy(B)
    for j in range(M) :
        if sub_arr[j] in B_copy :
            equal_cnt += 1
            B_copy.remove(sub_arr[j])
    if equal_cnt == M :
        ans_cnt += 1


print(ans_cnt)