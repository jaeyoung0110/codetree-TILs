N = int(input())
set_1 = list(map(int,input().split()))
set_2 = list(map(int,input().split()))

ans_cnt = 0

for i in range(N) : 
    for j in range(N) :
        for k in range(N) :
            # set_1 번과의 거리 확인
            is_ok = [False,False,False]
            # i 자리
            for ii in range(i-2,i+2+1) :
                # 원순열 보정
                if ii > N : ii = ii - N
                if ii < 1 : ii = N + ii
                # 값 거리 비교
                if ii == set_1[0] :
                    is_ok[0] = True
            for jj in range(j-2,j+2+1) :
                # 원순열 보정
                if jj > N : jj = jj - N
                if jj < 1 : jj = N + jj
                # 값 거리 비교
                if jj == set_1[1] :
                    is_ok[1] = True
            for kk in range(k-2,k+2+1) :
                # 원순열 보정
                if kk > N : kk = kk - N
                if kk < 1 : kk = N + kk
                # 값 거리 비교
                if kk == set_1[2] :
                    is_ok[2] = True
            if is_ok[0] == True and is_ok[1] == True and is_ok[2] == True :
                ans_cnt += 1
                continue
                
            # set_2 번과의 거리 확인
            is_ok = [False,False,False]
            # i 자리
            for ii in range(i-2,i+2+1) :
                # 원순열 보정
                if ii > N : ii = ii - N
                if ii < 1 : ii = N + ii
                # 값 거리 비교
                if ii == set_2[0] :
                    is_ok[0] = True
            for jj in range(j-2,j+2+1) :
                # 원순열 보정
                if jj > N : jj = jj - N
                if jj < 1 : jj = N + jj
                # 값 거리 비교
                if jj == set_2[1] :
                    is_ok[1] = True
            for kk in range(k-2,k+2+1) :
                # 원순열 보정
                if kk > N : kk = kk - N
                if kk < 1 : kk = N + kk
                # 값 거리 비교
                if kk == set_2[2] :
                    is_ok[2] = True
            if is_ok[0] == True and is_ok[1] == True and is_ok[2] == True :
                ans_cnt += 1

print(ans_cnt)

# def is_pass(i,idx) :
#     for ii in range(i-2,i+2+1) :
#         # 원순열 보정
#         if ii > N : ii = ii - N
#         if ii < 1 : ii = N + ii
#         # 값 거리 비교
#         if ii == set_1[0] :
#             is_ok = True