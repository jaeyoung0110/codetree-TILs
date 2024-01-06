import copy

a = list(input())

max_val = 0

for i in range(len(a)) :
    a_copy = copy.deepcopy(a)
    if a_copy[i] == '1' :
        a_copy[i] = '0'
    else :
        a_copy[i] = '1'
    b = int(int(''.join(a_copy),2))
    max_val = max(max_val, b)

print(max_val)