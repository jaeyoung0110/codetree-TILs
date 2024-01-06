S = input()


cnt_b = 0

for i in range(len(S)-1) :
    for j in range(i+1, len(S)) :
        if S[i] == '(' and S[j] == ')' :
            cnt_b += 1

print(cnt_b)