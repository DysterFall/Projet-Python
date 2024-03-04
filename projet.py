class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass

class MyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top = -1

    def add_to_stack(self, item):
        if self.top >= self.max_size - 1:
            raise MyOutOfSizeException("MyOutOfSizeException")
        self.top += 1
        setattr(self, f'item_{self.top}', item)

    def pop_from_stack(self):
        if self.top == -1:
            raise MyEmptyStackException("MyEmptyStackException")
        item = getattr(self, f'item_{self.top}')
        delattr(self, f'item_{self.top}')
        self.top -= 1
        return item

    def is_full(self):
        return self.top >= self.max_size - 1

    def is_empty(self):
        return self.top == -1

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
