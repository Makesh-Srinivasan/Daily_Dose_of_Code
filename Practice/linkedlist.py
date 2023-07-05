#class Node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#class linkedlist
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = node

    def print(self):
        if self.head is None:
            print("The linkedlist is empty.")
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        
ll = LinkedList()

ll.insert(Node(1))
ll.insert(Node(21))
ll.insert(Node(3))
ll.insert(Node(42))
ll.insert(Node(55))

ll.print()



