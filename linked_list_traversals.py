class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self,nodes):
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

    def traverse(self,pos):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def get(self,pos):
        idx = 0
        for idx,node in enumerate(self):
            if idx == pos:
                return node
            idx+=1
        raise Exception(f"Index Error : Index {pos} not found")

    def reverse(self):
        prev = None
        current_node = self.head
        while(current_node is not None):
            next = current_node.next 
            current_node.next = prev
            prev = current_node
            current_node = next
        self.head = prev

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


llist = LinkedList(["Aaron", "Bob", "Cathy", "Dawson", "Elm"])
#print(llist.get(int(input())))
print(llist)
llist.reverse()
print(llist)
#print(llist)

