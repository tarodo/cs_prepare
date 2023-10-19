from typing import Optional
from base import upload_list, ListNode, print_linked_list, connect_two_lists


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next:
        return head
    next_el = head
    cur_el = head.next
    prev_el = head.next.next
    next_el.next = None
    while prev_el:
        cur_el.next = next_el
        next_el = cur_el
        cur_el, prev_el = prev_el, prev_el.next
    cur_el.next = next_el
    return cur_el


nums = upload_list([1, 2])
print_linked_list(reverseList(nums))
