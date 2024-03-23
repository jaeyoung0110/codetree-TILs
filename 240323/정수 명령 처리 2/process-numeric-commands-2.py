from collections import deque

class Queue :
    def __init__(self) :
        self.dq = deque()
    
    def push(self,item) :
        self.dq.append(item)

    def empty(self) :
        return not self.dq

    def size(self) :
        return len(self.dq)
    
    def pop(self) :
        if self.empty()  :
            raise Exception("Queue is empty")
        
        return self.dq.popleft()
    
    def front(self) :
        if self.empty() :
            raise Exception("Queue is empty")

        return self.dq[0]


# 1
N = int(input())
q = Queue()
for i in range(N) :
    str = input()
    if str.startswith("push") :
        q.push(str.split()[1])
    elif str.startswith("empty") :
        print(int(q.empty()))
    elif str.startswith("size") :
        print(q.size())
    elif str.startswith("pop") :
        print(q.pop())
    else :
        print(q.front())
# 2

# 3