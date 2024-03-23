# 0


# 1
s = input()

# 2
ans = True
stack = []
for i in s :
    if i == '(' :
        stack.append(i)
    elif i == ')' :
        if len(stack) == 0 :
            ans = False
        else :
            stack.pop()
if len(stack) != 0 :
    ans = False

# 3
if ans :
    print("Yes")
else :
    print("No")