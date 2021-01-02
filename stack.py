

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
        
    def push(self, item):
        new_node = Node(item)

        if self.isEmpty():
            self.head = new_node

        self.head.next = new_node
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            print("Underflow")

        