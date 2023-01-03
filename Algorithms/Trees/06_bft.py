from collections import deque

from Algorithms.Trees.base import create_bst


def level_order_traversal(root):
    result_str = ""
    q1 = deque()
    q2 = deque()
    q1.append(root)

    def clear_queue(cur_q, help_q):
        result = []
        while cur_q:
            el = cur_q.popleft()
            if el.left:
                help_q.append(el.left)
            if el.right:
                help_q.append(el.right)
            result.append(str(el.data))
        return result

    while q1 or q2:
        if q1:
            result = clear_queue(q1, q2)
        else:
            result = clear_queue(q2, q1)

        result_str += " ".join(result) + " "
    result_str = result_str[:-1]

    print(result_str)
    return result_str


arr = [100, 50, 200, 25, 75, 350]
root = create_bst(arr)
print("\nLevel Order Traversal:\n", end="")
level_order_traversal(root)
