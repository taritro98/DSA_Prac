# Python3 program to demonstrate linked list 
# based implementation of queue 
  
# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
# A class to represent a queue 
  
# The queue, front stores the front node 
# of LL and rear stores ths last node of LL 
class MyQueue: 
      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    # Method to add an item to the queue 
    def push(self, item): 
        temp = Node(item) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
  
    # Method to remove an item from queue 
    def pop(self): 
          
        if self.isEmpty(): 
            return -1
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None
        return str(temp.data)