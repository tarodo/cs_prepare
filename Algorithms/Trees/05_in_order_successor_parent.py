def inorder_successor_bst_parent_pointer(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    while node.parent:
        if node.parent.left == node:
            return node.parent
        node = node.parent
    return


def find_successor(root, d):
    while root:
        if root.data < d:
            root = root.right
        elif root.data > d:
            root = root.left
        else:
            return inorder_successor_bst_parent_pointer(root)
    return
