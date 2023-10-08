from typing import Optional

from base import upload_list, ListNode, connect_loop_list, connect_two_lists

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    cur_n = 0
    cur_el = head.next
    control_el = None
    if not cur_el and n == 1:
        return None
    while cur_el:
        if cur_n < n:
            control_el = head
            cur_n += 1
        else:
            control_el = control_el.next
        cur_el = cur_el.next
    if cur_n >= n:
        if control_el.next and control_el.next.next:
            control_el.next = control_el.next.next
        else:
            control_el.next = None
    elif cur_n == n - 1:
        return head.next
    return head

nums = upload_list([1,2])
ttt = removeNthFromEnd(nums, 2)
print(ttt)
