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

    def kth_value(self, k):
        current_node = self.head
        found_node = self.head
        dist = 0

        while current_node:
            if dist > k:
                found_node = found_node.next
            current_node = current_node.next
            dist += 1

        if dist > k:
            return found_node.values
        else:
            raise ValueError("the list is shorter than the given value")


    def zip_list(self, a, b):
        a_current = a.head
        b_current = b.head

        while a_current and b_current:

            a_next = a_current.next
            a_current.next = b_current
            a_current = a_next

            b_next = b_current.next
            b_current.next = a_current
            b_current = b_next

            if a_current.next is None:
                a_current.next = b_current
                return a
        return a
