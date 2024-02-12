# 1
N = int(input())

# 2
class DLL :
    def __init__(self) :
        self.head = None
        self.tail = None
        self.node_num = 0
    
    def push_front(self, data) :
        new_node = Node(data)

        if self.node_num == 0 :
            self.head = new_node
            self.tail = new_node
        else :
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.node_num += 1
    
    def push_back(self, data) :
        # 새거 만들기
        new_node = Node(data)
        
        if self.node_num == 0 :
            # 헤드 테일 처리
            self.head = new_node
            self.tail = new_node
        else :
            # 새 노드 처리
            new_node.prev = self.tail
            # 테일 노드 처리
            self.tail.next(new_node)
            self.tail = new_node
        self.node_num += 1
    
    def pop_front(self) :
        # return data 가져오기
        pop_data = self.head.data
            
        if self.node_num == 1 :
            self.head = None
            self.tail = None
        
        else :
            self.head = self.head.next
            self.head.prev = None
        
        self.node_num -= 1
        return pop_data

    def pop_back(self) :
        # return data 가져오기
        pop_data = self.tail.data
            
        if self.node_num == 1 :
            self.head = None
            self.tail = None
        
        else :
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.node_num -= 1
        return pop_data

    def size(self) :
        return self.node_num

    def empty(self) :
        if self.node_num == 0 : return 1
        else : return 0

    def front(self) :
        return self.head.data

    def back(self) :
        return self.tail.data

class Node :
    def __init__(self, data) :
        self.data = data
        self.prev = None
        self.next = None
    
# 3

DLL1 = DLL()

for _ in range(N) :
    command = input()
    if command.startswith("push_front") :
        c, d = command.split()
        DLL1.push_front(d)

    elif command.startswith("push_back") :
        c, d = command.split()
        DLL1.push_back(d)
    
    elif command.startswith("pop_front") :
        print(DLL1.pop_front())

    elif command.startswith("pop_back") :
        print(DLL1.pop_back())
    
    elif command.startswith("size") :
        print(DLL1.size())
    
    elif command.startswith("empty") :
        print(DLL1.empty())

    elif command.startswith("front") :
        print(DLL1.front())

    elif command.startswith("back") :
        print(DLL1.back())