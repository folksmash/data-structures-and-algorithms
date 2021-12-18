from linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList

def test_empty_list():
    empty_list = LinkedList()
    assert empty_list.head == None

def test_node_exists():
    assert Node

def test_create_node():
    new_node = Node('stuff')
    assert new_node.values == 'stuff'
    assert new_node.next == None

def test_insert_node():
    new_head = Node('stuff')
    assert new_head.values == 'stuff'
    assert new_head.next == None


def test_includes_true():
    lst = LinkedList()
    lst.insert("dog")
    lst.insert("cat")
    actual = lst.includes("dog")
    expected = True
    assert actual == expected


def test_includes_false():
    lst = LinkedList()
    lst.insert("dog")
    lst.insert("cat")
    actual = lst.includes("ball")
    expected = False
    assert actual == expected

def test_to_string():
    lst = LinkedList()
    lst.insert("dog")
    lst.insert("cat")
    assert str(lst) == "{ cat } -> { dog } -> NULL"


def test_append_end():
    list = LinkedList()
    list.insert("1")
    list.append("2")
    assert str(list) == "{ 1 } -> { 2 } -> NULL"

def test_insert_before():
    list = LinkedList()
    list.insert("1")
    list.insert("2")
    list.insert("4")
    list.insert("5")
    list.insert_before("3", 2)
    assert str(list) == "{ 5 } -> { 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL"

def test_insert_after():
    list = LinkedList()
    list.insert("1")
    list.insert("2")
    list.insert("4")
    list.insert("5")
    list.insert_before("3",2)
    assert str(list) == "{ 5 } -> { 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL"

def test_append_multi_end():
    list = LinkedList()
    list.append("1")
    list.append("2")
    list.append("3")
    assert str(list) == "{ 1 } -> { 2 } -> { 3 } -> NULL"

