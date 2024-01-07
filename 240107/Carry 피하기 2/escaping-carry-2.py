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
            for l in range(1,max_len+1) :
                try :
                    if (int(data_int[i][-l]) + int(data_int[j][-l]) + int(data_int[k][-l])) // 10 >= 1 :
                        is_carry = True
                except :
                    pass
            if is_carry == False :
                max_int = max(max_int, sum_int)

print(max_int)