N = int(input())
coo = [0 for _ in range(101)]

# 좌표에 데이터 입력
for _ in range(N) :
    loc, idx = input().split()
    coo[int(loc)] = idx

# 사진 판단
max_len = 0

for i in range(101) : # i = 사진 시작 위치
    for j in range(i+1, 101) : # j = 사진 끝 위치
        cnt_G = 0
        idx_G = [0,0]
        cnt_H = 0
        idx_H = [0,0]
        for k in range(i,j+1) : # i~j 까지 구간 탐색
            if coo[k] == 'G' : 
                cnt_G += 1
                if cnt_G == 1 :
                    idx_G[0] = k
                    idx_G[1] = k
                else :
                    idx_G[1] = k
            elif coo[k] == 'H' : 
                cnt_H += 1
                if cnt_H == 1 :
                    idx_H[0] = k
                    idx_H[1] = k
                else :
                    idx_H[1] = k
        # G H 값 동일
        if cnt_G == cnt_H and cnt_G > 0 and cnt_H > 0 :
            max_len = max(max_len, max(idx_G[1],idx_H[1])-min(idx_G[0],idx_H[0]))
        # G 만
        elif cnt_G > 0 and cnt_H == 0 :
            max_len = max(max_len, idx_G[1] - idx_G[0])
        # H 만
        elif cnt_G == 0 and cnt_H > 0 :
            max_len = max(max_len, idx_H[1] - idx_H[0])



print(max_len)