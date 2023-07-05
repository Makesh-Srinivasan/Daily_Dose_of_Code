# Node class
# LinkedList class
#   insert
#   print

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newnode):
        if self.head is None:
            self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newnode
    
    def insert_at_head(self, newhead):
        if self.head is None:
            self.head = newhead
        else:
            temp = self.head
            self.head = newhead
            newhead.next = temp

    def count(self):
        count = 0
        lastnode = self.head
        while lastnode:
            count += 1
            lastnode = lastnode.next
        return count
    
    def insert_at_index(self, newnode, index):
        if index == 0:
            print("you are inserting at HEAD")
            self.insert_at_head(newnode)
            return

        count = 0
        nodeatindex = self.head
        while True:
            if count == index-1:
                break
            nodeatindex = nodeatindex.next
            count += 1
        temp = nodeatindex.next
        nodeatindex.next = newnode
        newnode.next = temp

    def print(self):
        if self.head is None:
            print("The LL is empty.")
            return
        currentnode = self.head
        while currentnode:
            print(currentnode.data, end="->")
            currentnode = currentnode.next
        print("||")
            


ll = LinkedList()
ll.insert(Node(2))
ll.insert(Node(3))
ll.insert_at_head(Node(1)) # change this to be the HEAD
ll.insert(Node(5))
ll.print()

ll.insert_at_index(Node(4), 3)
ll.print()

