class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(current_node, sequence):
    if not current_node:
        return False
    if not sequence:
        return False
    find_el = sequence[0]
    if not current_node.left and not current_node.right:
        if current_node.val == find_el:
            return True

    return find_path(current_node.left, sequence[1:]) or find_path(
        current_node.right, sequence[1:]
    )


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


if __name__ == "__main__":
    main()
