from collections import deque

from Algorithms.Trees.base import create_bst


def traverse(root):
    result = deque()

    queue = deque()
    queue.append(root)
    while queue:
        cur_level = []
        for _ in range(len(queue)):
            el = queue.popleft()
            cur_level.append(el.data)
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)

        result.appendleft(cur_level)

    return result


arr = [100, 50, 200, 25, 75, 350]
root = create_bst(arr)

print(traverse(root))