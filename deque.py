from collections import deque


llist = deque("abcde")
llist.append('f')
llist.pop()
print(llist)