from Node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value): # add new node to the queue
        
        # create new node
        node = Node(value)

        # if the queue is empty
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self): #getting the first element entered the queue

        # if the queue is empty
        if self.front == None:
            return "This queue is empty"
        
        # if the queue contains only one element
        if self.front == self.rear:
            self.rear = None
        
        temp = self.front
        self.front = self.front.next
        temp.next = None

        return temp.value

    def peek(self):

        if self.front == None:
            return "this queue is empty"
        return self.front.value


