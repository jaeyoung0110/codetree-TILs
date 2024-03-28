import sys

n = int(input())
arr = list(map(int,input().split()))

sub_sum = 0
max_sum = -sys.maxsize
for i in arr :
    if sub_sum >= 0 : sub_sum += i
    else : sub_sum = i
    max_sum = max(max_sum,sub_sum)

print(max_sum)