n = int(input())
data_int = []
for i in range(n) :
    data_int.append(input())

max_int = -1
is_carry = False

for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            is_carry = False
            sum_int = int(data_int[i]) + int(data_int[j]) + int(data_int[k])
            max_len = max(len(data_int[i]),len(data_int[j]),len(data_int[k]))
            # 자리수 맞추기
            for l in [i,j,k] :
                while len(data_int[l]) < max_len :
                    data_int[l] = '0' + data_int[l]

            # 자리수 합 캐리 여부
            for l in range(1,max_len+1) :
                if (int(data_int[i][-l]) + int(data_int[j][-l]) + int(data_int[k][-l])) // 10 >= 1 :
                    is_carry = True
            if is_carry == False :
                max_int = max(max_int, sum_int)

print(max_int)