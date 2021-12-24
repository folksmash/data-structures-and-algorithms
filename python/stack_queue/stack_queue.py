class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None


    def push(self, value):
        self.top = Node(value, self.top)


    def pop(self):
        if not self.top:
            raise Exception

        temp = self.top
        self.top = self.top.next

        return temp.value


    def is_empty(self):
        return self.top is None


    def peek(self):
        if not self.top:
            raise Exception
        return self.top.value


class Queue:
    def __init__(self):
        self.front = None
        self.back = None


    def enqueue(self, value):
        node = Node(value)

        if not self.back:
            self.back = node
            self.front = node

        self.back.next = node


    def dequeue(self):
        if not self.front:
            raise Exception


        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value


    def peek(self):
        if not self.front:
            raise Exception
        return self.front.value


    def is_empty(self):
        return self.front is None
