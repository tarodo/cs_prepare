def are_identical(root1, root2):
    if not root1 and not root2:
        return True

    if root1 and root2 and root1.data == root2.data:
        if are_identical(root1.left, root2.left) and are_identical(root1.right, root2.right):
            return True

    return False
