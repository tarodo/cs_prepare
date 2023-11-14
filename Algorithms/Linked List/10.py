class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insert_val: int) -> 'Node':
        node = Node(insert_val)

        if not head:
            node.next = node
            return node

        prev, curr = head, head.next

        while prev.next != head:
            if prev.val <= node.val <= curr.val:
                break

            if prev.val > curr.val and (node.val > prev.val or node.val < curr.val):
                break

            prev, curr = prev.next, curr.next

        node.next = curr
        prev.next = node

        return head
