from collections import deque

from Algorithms.Trees.base import create_bst


def traverse(root):
    order_right = True
    result = []
    q = deque()
    q.append(root)
    while q:
        level_result = []
        level_len = len(q)
        for _ in range(level_len):
            if order_right:
                el = q.popleft()
            else:
                el = q.pop()

            if el.left:
                q.append(el.left)
            if el.right:
                q.append(el.right)

            level_result.append(el.data)
        result.append(level_result)

    return result


arr = [100, 50, 200, 25, 75, 350]
root = create_bst(arr)

print(traverse(root))
