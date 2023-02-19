class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths_recursive(current_node, required_sum, current_path, all_paths):
    if not current_node:
        return

    current_path.append(current_node.val)

    if current_node.val == required_sum and not current_node.left and not current_node.right:
        all_paths.append(list(current_path))
    else:
        new_sum = required_sum - current_node.val
        find_paths_recursive(current_node.left, new_sum, current_path, all_paths)
        find_paths_recursive(current_node.right, new_sum, current_path, all_paths)

    del current_path[-1]


def find_paths(root, required_sum):
    all_paths = []
    find_paths_recursive(root, required_sum, [], all_paths)
    return all_paths


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print("Tree paths with required_sum " + str(required_sum) +
          ": " + str(find_paths(root, required_sum)))


main()
