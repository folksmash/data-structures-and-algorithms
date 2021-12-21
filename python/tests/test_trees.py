from trees.binary_tree import BinaryTree
from trees.node import Node




# DONE: Can successfully instantiate an empty tree
def test_binary_tree_empty():
    tree = BinaryTree()
    assert tree


# DONE: Can successfully instantiate a tree with a single root node
def test_binary_tree_with_root():
    spam = Node("spam")
    tree = BinaryTree(spam)
    actual = tree.root.value
    expected = "spam"
    assert actual == expected


# DONE: Can successfully return a collection from a preorder traversal
def test_pre_order():
    spam = Node("spam")
    spam.left = Node("banana")
    spam.right = Node("ketchup")
    tree = BinaryTree(spam)
    expected = ["spam", "banana", "ketchup"]
    actual = tree.pre_order()

    assert actual == expected


# DONE: Can successfully return a collection from an inorder traversal
def test_in_order():
    spam = Node("spam")
    spam.left = Node("banana")
    spam.right = Node("ketchup")
    tree = BinaryTree(spam)
    expected = ["banana", "spam", "ketchup"]
    actual = tree.in_order()

    assert actual == expected


# DONE: Can successfully return a collection from a postorder traversal
def test_post_order():
    spam = Node("spam")
    spam.left = Node("banana")
    spam.right = Node("ketchup")
    tree = BinaryTree(spam)
    expected = ["banana", "ketchup", "spam"]
    actual = tree.post_order()

    assert actual == expected

# DONE: Can successfully add a left child and right child to a single root node
def test_tree_left_right():
    tree = BinaryTree()
    tree.root = Node("root", left=Node("leftvalue"), right=Node("rightvalue"))
    assert tree.root.value == "root"
    assert tree.root.left.value == "leftvalue"
    assert tree.root.right.value == "rightvalue"
