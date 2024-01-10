# 초기 설정 단계 - 입력 출력 변수 설정
N = int(input())

datas_line = []
for _ in range(N) :
    datas_line.append(list(map(int,input().split())))

ans_cnt = 0

# 알고리즘 - 완전탐색
for target_line_idx in range(N) :
    is_overlap = False
    for compare_line_idx in range(N) :
        if target_line_idx == compare_line_idx : continue
        if (datas_line[target_line_idx][0] - datas_line[compare_line_idx][0])*(datas_line[target_line_idx][1] - datas_line[compare_line_idx][1]) < 0:
            is_overlap = True
    if is_overlap == False :
        ans_cnt += 1


# 정답 출력
print(ans_cnt)