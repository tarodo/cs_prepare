from Algorithms.Trees.base import create_bst
from collections import deque


def find_successor(root, key):
    flag = False
    queue = deque()
    queue.append(root)
    while queue:
        level_len = len(queue)
        for _ in range(level_len):
            el = queue.popleft()
            if flag:
                return el.data
            if el.data == key:
                flag = True
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)


arr = [100, 50, 200, 25, 75, 350]
root = create_bst(arr)

print(find_successor(root, 25))