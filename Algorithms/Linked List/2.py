from typing import Optional
from base import upload_list, ListNode, connect_loop_list


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    cur_node = head
    seen = set()
    while cur_node:
        if cur_node in seen:
            return cur_node

        seen.add(cur_node)
        cur_node = cur_node.next
    return None


nums = [3, 2, 0, -4]
pos = 1
listnode = upload_list(nums)
listnode = connect_loop_list(listnode, pos)
print(detectCycle(listnode))

nums = [1,2]
pos = 0
listnode = upload_list(nums)
listnode = connect_loop_list(listnode, pos)
print(detectCycle(listnode))

nums = []
listnode = upload_list(nums)
print(detectCycle(listnode))