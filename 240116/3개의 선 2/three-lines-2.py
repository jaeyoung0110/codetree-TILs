# 1
N = int(input())
dots = []
for _ in range(N) :
    dots.append(list(map(int,input().split())))

is_possible = False

# 2 
# case 1 : x 3
for i in range(11) :
    for j in range(i+1, 11) :
        for k in range(j+1, 11) :
            is_ok = True
            for dot in dots :
                if dot[0] not in [i,j,k] :
                    is_ok = False
                    break
            if is_ok == True :
                is_possible = True
# case 2 : x 2 y 1
for i in range(11) :
    for j in range(i+1, 11) :
        for k in range(11) :
            is_ok = True
            for dot in dots :
                if dot[0] not in [i,j] and dot[1] != k :
                    is_ok = False
                    break
            if is_ok == True :
                is_possible = True

# case 3 : x 1 y 2
for i in range(11) :
    for j in range(i+1, 11) :
        for k in range(11) :
            is_ok = True
            for dot in dots :
                if (dot[1] not in [i,j]) and (dot[0] != k) :
                    is_ok = False
                    break
            if is_ok == True :
                is_possible = True

# case 4 : y 3
for i in range(11) :
    for j in range(i+1, 11) :
        for k in range(j+1, 11) :
            is_ok = True
            for dot in dots :
                if dot[1] not in [i,j,k] :
                    is_ok = False
                    break
            if is_ok == True :
                is_possible = True

# 3
if is_possible == True :
    print(1)
else :
    print(0)