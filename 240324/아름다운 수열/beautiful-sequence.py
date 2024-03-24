## 1
N = int(input())
arrN = []
for _ in range(N) :
    arrN.append(int(input()))
M = int(input())
arrM = []
for _ in range(M) :
    arrM.append(int(input()))

## 2
# 첫수열에서 두번째수열 길이만큼 완전탐색 하면서
# 첫부분수열과 두번째수열을 정렬한뒤
# 두 수열의 모든 원소의 차이를 계산한 결과가 모두 똑같으면 참
# 그 때의 인덱스 기록 및 개수 추가
ans_cnt = 0
ans_idx_arr = []
arrM.sort()
for i in range(N-M+1) :
    subN = []
    for j in range(i,i+M) :
        subN.append(arrN[j])
    subN.sort()

    gap = subN[0] - arrM[0]
    is_true = True
    for k in range(M) :
        if subN[k] - arrM[k] != gap :
            is_true = False
    
    if is_true :
        ans_cnt += 1
        ans_idx_arr.append(i+1)


## 3
print(ans_cnt)
for i in ans_idx_arr :
    print(i)