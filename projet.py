class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.top = None
        self.size = 0

    def add_to_stack(self, item):
        if self.size >= self.max_size:
            raise MyOutOfSizeException("MyOutOfSizeException")
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop_from_stack(self):
        if self.size == 0:
            raise MyEmptyStackException("MyEmptyStackException")
        item = self.top.value
        self.top = self.top.next
        self.size -= 1
        return item

    def is_full(self):
        return self.size >= self.max_size

    def is_empty(self):
        return self.size == 0

if __name__ == '__main__':
    myStack = MyStack(3)
    myStack.add_to_stack('hello')
    myStack.add_to_stack('hello')
    print(myStack.is_full()) 
    myStack.add_to_stack('hello')
    print(myStack.is_full())  
    try:
        myStack.add_to_stack('hello')  
    except MyOutOfSizeException as e:
        print(e)
    print(myStack.pop_from_stack())  
    print(myStack.is_empty())  
    print(myStack.pop_from_stack())  
    print(myStack.is_empty())  
    print(myStack.pop_from_stack())  
    print(myStack.is_empty()) 
    try:
        print(myStack.pop_from_stack())  
    except MyEmptyStackException as e:
        print(e)