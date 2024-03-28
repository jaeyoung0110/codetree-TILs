n, k = map(int,input().split())
value = []
for _ in range(n) :
    value.append(int(input()))

value.sort(reverse = True)

cnt_coin = 0
for i in value :
    cnt_coin += k//i
    k = k % i

print(cnt_coin)