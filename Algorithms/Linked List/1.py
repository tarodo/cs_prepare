from typing import Optional
from base import upload_list, ListNode, connect_loop_list


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


nums = [3, 2, 0, -4]
pos = 1
listnode = upload_list(nums)
listnode = connect_loop_list(listnode, pos)
print(hasCycle(listnode))

nums = [1,2]
pos = 0
listnode = upload_list(nums)
listnode = connect_loop_list(listnode, pos)
print(hasCycle(listnode))

nums = []
listnode = upload_list(nums)
print(hasCycle(listnode))