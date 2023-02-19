from Algorithms.Trees.base import create_bst

current_count = 0


def find_nth_highest_in_bst(node, n):
    global current_count

    if not node:
        return None

    result = find_nth_highest_in_bst(node.right, n)
    if result:
        return result

    current_count = current_count + 1

    if n == current_count:
        return node

    result = find_nth_highest_in_bst(node.left, n)
    if result:
        return result

    return None


arr = [100, 50, 200, 25, 75, 125, 350]
root = create_bst(arr)
print(find_nth_highest_in_bst(root, 3).data)
