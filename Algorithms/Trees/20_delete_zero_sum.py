from Algorithms.Trees.base import BinaryTreeNode, display_level_order


def delete_zero_sum_subtree_rec(root):
    if not root:
        return 0

    sum_left = delete_zero_sum_subtree_rec(root.left)
    sum_right = delete_zero_sum_subtree_rec(root.right)

    if sum_left == 0:
        root.left = None

    if sum_right == 0:
        root.right = None

    return root.data + sum_left + sum_right


def delete_zero_sum_subtree(root):
    if root:
        if delete_zero_sum_subtree_rec(root) == 0:
            root = None


def create_test_tree1():
    head = BinaryTreeNode(7)
    curr_head = head

    left = BinaryTreeNode(5)
    right = BinaryTreeNode(6)
    curr_head.left = left
    curr_head.right = right

    curr_head = head.left
    left = BinaryTreeNode(-3)
    right = BinaryTreeNode(-2)
    curr_head.left = left
    curr_head.right = right

    return head


root = create_test_tree1()
print("Level Order Traversal:")
display_level_order(root)

delete_zero_sum_subtree(root)
print("Level Order Traversal:")
display_level_order(root)
