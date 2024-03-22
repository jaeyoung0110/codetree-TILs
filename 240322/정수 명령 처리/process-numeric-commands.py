# 0
class Stack() :
    def __init__(self) :
        self.items = []

    def push(self, item) :
        self.items.append(item)

    def empty(self) :
        return not self.items

    def size(self) :
        return len(self.items)

    def pop(self) :
        if len(self.items) == 0 :
            raise Exception("Stack is empty")
        
        return self.items.pop()
    
    def top(self) :
        if len(self.items) == 0 :
            raise Exception("Stack is empty")
        
        return self.items[-1]

# 1
n = int(input())
stack = Stack()
for _ in range(n) :
    inputData = input().split()
    if inputData[0] == 'push' :
        stack.push(inputData[1])
    elif inputData[0] == 'empty' :
        print(int(stack.empty()))
    elif inputData[0] == 'size' :
        print(stack.size())
    elif inputData[0] == 'pop' :
        print(stack.pop())
    elif inputData[0] == 'top' :
        print(stack.top())
# 2


# 3