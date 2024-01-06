s = input()

ans_cnt = 0

for i in range(len(s)) :
    for j in range(i+1, len(s)-1) :
                if s[i] == '(' and s[i+1] == '(' and s[j] == ')' and s[j+1] == ')' :
                    ans_cnt += 1
print(ans_cnt)