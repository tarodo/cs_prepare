from typing import Optional
from base import upload_list, ListNode, print_linked_list, connect_two_lists


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    cur_el = head
    prev_el = ListNode(-1, cur_el)
    super_first = prev_el
    while cur_el:
        if cur_el.val == val:
            prev_el.next = cur_el.next
        else:
            prev_el = cur_el
        cur_el = cur_el.next

    return super_first.next




nums = upload_list([1,2,6,3,4,5,6])
new_head = removeElements(nums, 6)
print(new_head)

nums = upload_list([])
new_head = removeElements(nums, 6)
print(new_head)

nums = upload_list([7,7,7,7])
new_head = removeElements(nums, 7)
print(new_head)

nums = upload_list([1, 2])
new_head = removeElements(nums, 1)
print(new_head)