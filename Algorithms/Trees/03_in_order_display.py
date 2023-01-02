"""
Given a binary tree, write an iterative algorithm to traverse the tree in-order.
"""
from collections import deque

from base import BinaryTreeNode, create_bst


def inorder_iterative(root: BinaryTreeNode) -> str:
    result_arr = []
    q = deque()

    def collect(root: BinaryTreeNode):
        tmp = root
        while tmp:
            q.append(tmp)
            tmp = tmp.left

    collect(root)

    while q:
        el = q.pop()
        result_arr.append(str(el.data))
        collect(el.right)

    return " ".join(result_arr)


arr = [25, 125, 200, 300, 75, 50, 12, 35, 60, 75]
root = create_bst(arr)

print(inorder_iterative(root))
