from Algorithms.Trees.base import create_bst


def print_left_perimeter(root, result):
    while root:
        curr_val = root.data
        if root.left:
            root = root.left
        elif root.right:
            root = root.right
        else:
            break
        result.append(str(curr_val) + " ")


def print_right_perimeter(root, result):
    r_values = []
    while root:
        curr_val = root.data

        if root.right:
            root = root.right
        elif root.left:
            root = root.left
        else:
            break
        r_values.append(curr_val)

    while len(r_values) != 0:
        result.append(str(r_values.pop()) + " ")


def print_leaf_nodes(root, result):
    if root:
        print_leaf_nodes(root.left, result)
        if not root.left and not root.right:
            result.append(str(root.data) + " ")

        print_leaf_nodes(root.right, result)


def display_tree_perimeter(root):
    result = []
    if root:
        result.append(str(root.data) + " ")
        print_left_perimeter(root.left, result)
        if root.left or root.right:
            print_leaf_nodes(root, result)
        print_right_perimeter(root.right, result)
    return "".join(result)


arr = [100, 50, 200, 25, 60, 350, 10, 70, 400]
root = create_bst(arr)
print(display_tree_perimeter(root))
