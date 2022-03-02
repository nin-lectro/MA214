class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None or self.tail == None

    def add(self, item):
        self.head = Node(item, self.head)
        if self.empty():
            self.tail = self.head

    def removeFront(self):
        if not self.empty():
            front = self.head.item
            self.head = self.head.next

            # this works as my empty()
            # checks if head OR tail is None
            if self.empty():
                self.tail = None
            return front

    def removeEnd(self):
        if not self.empty():
            # one element list
            if self.head == self.tail:
                back = self.tail.item
                self.head, self.tail = None, None
            # if more than one element
            else:
                pointer = self.head
                while pointer.next != self.tail:
                    pointer = pointer.next
                back = pointer.next.item
                pointer.next = None
                self.tail = pointer
            return back

