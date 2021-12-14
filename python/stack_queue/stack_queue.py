class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.front = None
    def peek(self):
        if self.front is None:
            return 'Empty'
        return self.front.value
    def push(self, value):
        self.front = Node(value, self.front)
    def pop(self):
        if self.front is None:
            return 'Empty'
        value = self.front.value
        return value
