class Node:

    def __init__(self, value, next = None):
        self.values = value
        self.next = next


class LinkedList:
    """
    Put docstring here
    """
    def __init__(self):
        self.head = None


    def insert(self, value):
        self.head = Node(value, self.head)


    def append(self, value):
        current = self.head
        if current:
            while current.next != None:
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value, self.head)


    def insert_before(self, value, position):
        new = Node(value)
        pointer = self.head
        counter = 1
        if position == 0:
            new.next = self.head
            self.head = new
            return self.head
        while pointer.next is not None:
            if counter == position:
                new.next = pointer.next
                pointer.next = new
                break
            counter += 1
            pointer = pointer.next
        return self.head


    def insert_after(self, value, position):
        new = Node()
        pointer = self.head
        counter = 1
        if position == 0:
            new.next = self.head
            self.head = new
            return self.head
        while pointer.next is not None:
            if counter == position:
                new.next = pointer.next
                pointer.next = new
                break
            counter += 1
            pointer = pointer.next
        return self.head


    def includes(self, value):
        current = self.head

        while current:
            if current.values == value:
                return True
            current = current.next
        return False


    def __str__(self):
        current = self.head
        output = ""
        while current:
            output += "{ " + current.values + " } -> "
            current = current.next
        output += "NULL"

        return output
