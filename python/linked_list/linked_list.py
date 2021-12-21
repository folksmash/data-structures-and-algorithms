# Create a Linked List class --
# Within your Linked List class, include a head property. --
# Upon instantiation, an empty Linked List should be created. --

# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

# self.head = node('dog', self.head)


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

#     includes
# Arguments: value
# Returns: Boolean
# Indicates whether that value exists as a Node’s value somewhere within the list.
    def includes(self, value):
        current = self.head

        while current:
            if current.values == value:
                return True
            current = current.next
        return False

# The class should contain the following methods
# insert
# Arguments: value
# Returns: nothing
# Adds a new node with that value to the head of the list with an O(1) Time performance.

    def __str__(self):
        current = self.head
        output = ""
        while current:
            output += "{ " + current.values + " } -> "
            current = current.next
        output += "NULL"

        return output

# to string
# Arguments: none
# Returns: a string representing all the values in the Linked List, formatted as:
# "{ a } -> { b } -> { c } -> NULL"
