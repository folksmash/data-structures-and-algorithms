from trees.binary_tree import BinaryTree
from trees.node import Node

def test_exists():
    assert BinaryTree
    assert Node

def test_tree_find_max():
    tree = BinaryTree()
    node = Node(10)
    tree.root = node

    node = Node(20)
    tree.root.left = node

    node = Node(30)
    tree.root.right = node

    node = Node(40)
    tree.root.left.right = node

    i = tree.find_max_value(tree.root)

    assert i == 40
