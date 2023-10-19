from typing import Optional


class MyLinkedList:

    def __init__(self):
        self.val = -1
        self.next_el = None

    def get(self, index: int) -> int:
        el = self
        for idx in range(index):
            if el.next_el:
                el = el.next_el
            else:
                return -1
        return el.val

    def addAtHead(self, val: int) -> None:
        if self.val == -1:
            self.val = val
            return
        new_el = MyLinkedList()
        new_el.val = self.val
        new_el.next_el = self.next_el
        self.val = val
        self.next_el = new_el

    def addAtTail(self, val: int) -> None:
        if self.val == -1:
            self.val = val
            return

        el = self
        while el.next_el:
            el = el.next_el
        new_el = MyLinkedList()
        new_el.val = val
        el.next_el = new_el

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        cur_el = self
        for idx in range(1, index):
            if cur_el.next_el:
                cur_el = cur_el.next_el
            else:
                return
        next_el = cur_el.next_el
        new_el = MyLinkedList()
        new_el.val = val
        new_el.next_el = next_el
        cur_el.next_el = new_el

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.next_el:
                self.val = self.next_el.val
                self.next_el = self.next_el.next_el
            else:
                self.val = -1
            return
        cur_el = self
        for idx in range(1, index):
            if cur_el.next_el:
                cur_el = cur_el.next_el
            else:
                return
        if cur_el.next_el:
            cur_el.next_el = cur_el.next_el.next_el


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class ListNode:
    def __init__(self, val, next_el=None):
        self.val = val
        self.next = next_el

    def get(self, index: int):
        el = self
        for idx in range(index):
            if el.next:
                el = el.next
            else:
                return None
        return el

    def __str__(self):
        return str(self.val)

def upload_list(elements):
    node = prev_node = None
    for el in elements[::-1]:
        node = ListNode(el)
        if prev_node:
            node.next = prev_node
        prev_node = node
    return node


def connect_loop_list(head_node, el):
    tail_node = head_node
    while tail_node.next:
        tail_node = tail_node.next

    con_node = head_node
    for i in range(el):
        con_node = head_node.next

    tail_node.next = con_node
    return head_node


def connect_two_lists(node_a: ListNode, node_b: ListNode):
    cur_b = node_b
    while cur_b.next:
        cur_b = cur_b.next
    cur_b.next = node_a


def print_linked_list(head: Optional[ListNode]):
    if not head:
        print("empty")
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(", ".join(result))
