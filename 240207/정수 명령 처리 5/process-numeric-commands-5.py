# 1
N = int(input())

# 2
arr = []

def push_back(n) :
    arr.append(int(n))
def pop_back() :
    arr.pop()
def size() :
    print(len(arr))
def get(k) :
    print(arr[int(k)-1])

for _ in range(N) :
    inp = list(input().split())
    if inp[0] == 'push_back' :
        push_back(inp[1])
    elif inp[0] == 'pop_back' :
        pop_back()
    elif inp[0] == 'size' :
        size()
    else :
        get(inp[1])