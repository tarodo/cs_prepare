from Algorithms.Trees.base import create_bst


def inorder_successor_bst(root, d):
    successor = None
    while root:
        if root.data < d:
            root = root.right
        elif root.data > d:
            successor = root
            root = root.left
        else:
            if root.right:
                successor = root.right
                while successor.left:
                    successor = successor.left
            break
    return successor


arr = [25, 125, 200, 350, 50, 75, 100]
root = create_bst(arr)


inorder_successor_bst(root, 25)
