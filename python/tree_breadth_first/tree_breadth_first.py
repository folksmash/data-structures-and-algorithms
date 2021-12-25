from collections import deque

def breadth_first(tree):
    queue = deque()
    initial_list = []

    if tree.root is None:
        return initial_list

    queue.appendleft(tree.root)

    while len(queue):
        front = queue.pop()

        initial_list.append(front.value)

        if front.left is not None:
            queue.appendleft(front.left)
        if front.right is not None:
            queue.appendleft(front.right)


    return initial_list
