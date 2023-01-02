import random
from collections import deque


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        self.next = None
        self.parent = None
        self.count = None


def insert(root, d):
    p_new = BinaryTreeNode(d)
    if not root:
        return p_new

    parent = None
    p_temp = root
    while p_temp:
        parent = p_temp
        if d < p_temp.data:
            p_temp = p_temp.left
        else:
            p_temp = p_temp.right

    if d < parent.data:
        parent.left = p_new
    else:
        parent.right = p_new

    return root


def find_in_bst(root, d):
    if not root:
        return None

    if root.data == d:
        return root
    elif root.data > d:
        return find_in_bst(root.left, d)
    else:
        return find_in_bst(root.right, d)


def find_node(root, d):
    if not root:
        return

    if root.data == d:
        return root

    temp = find_node(root.left, d)
    if temp:
        return temp

    return find_node(root.right, d)


def display_inorder(node):
    if not node:
        return

    display_inorder(node.left)
    print(str(node.data), end=", ")
    display_inorder(node.right)


def create_bst(arr):
    root = None
    for x in arr:
        root = insert(root, x)
    return root


def create_binary_tree(count):
    root = None
    for i in range(1, count):
        root = insert(root, random.randrange(1, 100))
    return root


def create_random_bst(count):
    root = None
    for i in range(1, count):
        root = insert(root, random.randrange(200, 300))
    return root


def bst_to_list_rec(root, lst):
    if not root:
        return

    bst_to_list_rec(root.left, lst)
    lst.append(root.data)
    bst_to_list_rec(root.right, lst)


def bst_to_list(root):
    lst = []
    bst_to_list_rec(root, lst)
    return lst


def insert_at_head(head, data):
    newNode = BinaryTreeNode(data)
    newNode.next = head
    return newNode


def populate_parents_rec(root, parent):
    if not root:
        return
    root.parent = parent

    populate_parents_rec(root.left, root)
    populate_parents_rec(root.right, root)


def populate_parents(root):
    populate_parents_rec(root, None)


def display_level_order(root):
    if not root:
        return
    q = deque()
    q.append(root)

    while q:
        temp = q.popleft()
        print(str(temp.data), end=",")
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    print()


def get_level_order(root):
    output = []
    if not root:
        return output

    q = deque()
    q.append(root)

    while q:
        temp = q.popleft()
        output.append(temp.data)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    return output


def get_inorder_helper(root, output):
    if not root:
        return output

    output = get_inorder_helper(root.left, output)
    output.append(root.data)
    output = get_inorder_helper(root.right, output)

    return output


def get_inorder(root):
    output = []
    return get_inorder_helper(root, output)


def is_identical_tree(root1, root2):
    if not root1 and not root2:
        return True

    if root1 and root2 and root1.data == root2.data:
        return is_identical_tree(root1.left, root2.left) and is_identical_tree(
            root1.right, root2.right
        )

    return False
