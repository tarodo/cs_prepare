from Algorithms.Trees.base import create_bst


def traverse(root):
    result = []
    from collections import deque

    queue = deque()
    queue.append(root)
    while queue:
        sum_level = 0
        level_len = len(queue)
        for _ in range(level_len):
            el = queue.popleft()
            sum_level += el.data
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)

        result.append(sum_level / level_len)

    return result


arr = [100, 50, 200, 25, 75, 350]
root = create_bst(arr)

print(traverse(root))
