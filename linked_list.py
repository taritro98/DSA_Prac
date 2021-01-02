class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self,nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def push(self,new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        self.head = new_node 

    def traverse(self):
        for node in self:
            print(node)

    def add_first(self,node):
        node.next = self.head
        self.head = node

    def add_end(self,node):
        if not self.head:
            raise Exception("List Empty")
        for current_node in self:
            pass
        current_node.next = node
    
    def add_after(self,target_node,node):
        if not self.head:
            raise Exception("List Empty")
        for current_node in self:
            if current_node.data == target_node:
                node.next = current_node.next
                current_node.next = node
                return
        
        raise Exception("Node with data '%s' not found" % target_node)

    def add_before(self, target_node, node):
        if not self.head:
            raise Exception("List Empty")

        if self.head.data == target_node:
            self.add_first(node)
        
        prev_node = self.head
        for current_node in self:
            if current_node.data == target_node:
                prev_node.next = node
                node.next = current_node
                return
            prev_node = current_node
        
        raise Exception(f"Node with data {target_node} not found")

    
    def remove_node(self, target_node):
        if not self.head:
            raise Exception("List Empty")

        if target_node == self.head.data:
            self.head = self.head.next
            return
        
        prev_node = self.head
        for current_node in self:
            if current_node.data == target_node:
                prev_node.next = current_node.next
                return
            prev_node = current_node
        
        raise Exception(f"Node with data {target_node} not found")

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


#llist = LinkedList(["a", "b", "c", "d", "e"])
#llist.add_first(Node('0'))
#llist.add_first(Node('1'))
#llist.add_end(Node('f'))
#llist.add_after("d",Node('g'))
#llist.add_before("c",Node('g'))
#llist.remove_node("a")
#llist.traverse()
#print(llist)

llist = LinkedList()
llist.push('a')
llist.push('b')
print(llist)

# ITER

# for node in llist:
#     print(node)

# first_node = Node("a")
# second_node = Node("b")
# third_node = Node("c")

# llist.head = first_node

# first_node.next=second_node
# second_node.next=third_node
# print(llist)