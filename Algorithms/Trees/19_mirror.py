from Algorithms.Trees.base import create_bst, display_level_order


def mirror_tree(root):
    if not root:
        return

    if root.left:
        mirror_tree(root.left)

    if root.right:
        mirror_tree(root.right)

    root.left, root.right = root.right, root.left

    return root


arr = [100, 50, 200, 25, 75, 125, 350]
root = create_bst(arr)

display_level_order(root)
mirror_tree(root)
print("\nMirrored Level Order Traversal:")
display_level_order(root)
