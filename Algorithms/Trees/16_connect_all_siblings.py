from Algorithms.Trees.base import create_bst, display_level_order


def populate_sibling_pointers(root):
    if not root:
        return

    current = root
    last = root

    while current:
        if current.left:
            last.next = current.left
            last = current.left
        if current.right:
            last.next = current.right
            last = current.right
        last.next = None
        current = current.next


def level_order_traversal_with_sibling(root):
    while root:
        print(str(root.data), end=",")
        root = root.next


v = [100, 50, 200, 25, 75, 300, 350]
root = create_bst(v)
display_level_order(root)
populate_sibling_pointers(root)
level_order_traversal_with_sibling(root)