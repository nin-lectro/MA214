class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head == None

    def pop(self):
        # pop from the beginning
        if not self.empty():
            popped_node = self.head
            self.head = self.head.next
            return popped_node.item

    def push(self, num):
        # push from the beginning
        new_head = Node(num, self.head)
        self.head = new_head


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def __len__(self):
        return self.n

    def empty(self):
        return len(self) == 0

    def enqueue(self, num):
        # we add the new node at the end of the list
        new_node = Node(num, None)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.n += 1

    def dequeue(self):
        if not self.empty():
            dequeued_node = self.head
            self.head = self.head.next
            self.n -= 1
            return dequeued_node.item


class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [LinkedList() for i in range(size)]

    def add(self, key):
        i = hash(key) % self.size
        self.keys[i].add(key)

    def delete(self, key):
        i = hash(key) % self.size
        self.keys[i].delete(key)

    def search(self, key):
        i = hash(key) % self.size
        return self.keys[i].search(key)


def main():
    pass


if __name__ == '__main__':
    main()
