class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass

class MyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack_size = 0
        self.top = -1


    def add_to_stack(self, item):
        if self.top >= self.max_size - 1:
            raise MyOutOfSizeException("MyOutOfSizeException")
        self.top += 1
        self.stack_size += 1

    def pop_from_stack(self):
        if self.top == -1:
            raise MyEmptyStackException("MyEmptyStackException")
        self.top -= 1
        self.stack_size -= 1
        return None

    def is_full(self):
        return self.stack_size == self.max_size

    def is_empty(self):
        return self.stack_size == 0

if __name__ == '__main__':
    max_size = int(input("Entrez la taille maximale de la pile MyStack: "))
    myStack = MyStack(max_size)
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
