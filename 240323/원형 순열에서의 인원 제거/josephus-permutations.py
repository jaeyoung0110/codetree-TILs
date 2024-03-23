from collections import deque
class Queue :
    def __init__(self) :
        self.q = deque()

    def push(self,item) :
        self.q.append(item)

    def size(self) :
        return len(self.q)
    
    def pop(self) :
        if len(self.q) == 0 :
            raise Exception("Q is empty")
        return self.q.popleft()
    
    def front(self) :
        if len(self.q) == 0 :
            raise Exception("Q is empty")
        return self.q[0]

#1
N, K = map(int,input().split())
q = Queue()
for i in range(N) :
    q.push(i+1)

#2
while q.size() != 1 :
    for _ in range(K-1) :
        q.push(q.pop())
    print(q.pop(), end=' ')
print(q.front())
#3