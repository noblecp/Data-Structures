class Stack:
    '''
    This class a Stack
    
    Basic operations include:
        - push() -> Inserts a new element at the top of the stack
        - pop() -> Removes and returns the element at the top of the stack
        - peek() -> Returns the element at the top of the stack but does not remove it
        - isEmpty() -> Returns True if the stack is empty and False otherwise

    Highlights:
        - adheres to LiFo ordering -> "Last in, First out"
        - does NOT allow offer constant time access to the i^th item
        - does allow constant time pushes and pops

    Use cases:
        - 
    '''
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return True if len(self.stack) == 0 else False
    
    def __str__(self):
        return(str(self.stack))