from Node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        
        # create a new node
        node = Node(value)

        # if the stack is not empty
        if self.top:
            node.next = self.top

        self.top = node
        self.size += 1

    def pop(self): # get off the top item
        
        if self.top is not None:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return "Stack is empty"
        
    def peek(self):
        
        if self.top:
            return self.top.value
        else:
            return " stack is empty"
        
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0


