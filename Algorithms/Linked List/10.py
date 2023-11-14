class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insert_val: int) -> 'Node':
        if head is None:
            new_node = Node(insert_val, None)
            new_node.next = new_node
            return new_node

        prev, curr = head, head.next
        to_insert = False

        while True:
            if prev.val <= insert_val <= curr.val:
                to_insert = True
            elif prev.val > curr.val:
                if insert_val >= prev.val or insert_val <= curr.val:
                    to_insert = True

            if to_insert:
                prev.next = Node(insert_val, curr)
                return head

            prev, curr = curr, curr.next
            if prev is head:
                break

        prev.next = Node(insert_val, curr)
        return head
