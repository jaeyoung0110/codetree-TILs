# 0
import sys


# 1
n_2 = input()
n_3 = input()

# 2
ans_arr = []
## 2진수 -> 10진수 모든 케이스

for i in range(len(n_2)) :
    copy_n_2 = list(n_2)
    copy_n_2[i] = str((int(copy_n_2[i])+1)%2)
    copy_n_2 = ''.join(copy_n_2)
    ans_arr.append(int(copy_n_2,2))
    

## 3진수 -> 10진수 모든 케이스
for i in range(len(n_3)) :
    copy_n_3 = list(n_3)
    for j in range(2) :
        copy_n_3 = list(copy_n_3)
        copy_n_3[i] = str((int(copy_n_3[i])+1)%3)
        copy_n_3 = ''.join(copy_n_3)
        if int(copy_n_3,3) in ans_arr :
            print(int(copy_n_3,3))
            sys.exit()
## 공통된게 답