from typing import Optional

from base import upload_list, ListNode, connect_loop_list, connect_two_lists


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    cur_a = headA
    cur_b = headB
    seen = set()
    while cur_a or cur_b:
        if cur_b and cur_b in seen:
            return cur_b
        if cur_a and cur_a in seen:
            return cur_a

        if cur_b:
            seen.add(cur_b)
            cur_b = cur_b.next
        if cur_a:
            if cur_a in seen:
                return cur_a
            seen.add(cur_a)
            cur_a = cur_a.next

    return None


nums = [31, 32, 33, 34]
nums2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
pos = 0
list_a = upload_list(nums)
list_b = upload_list(nums2)
connector = list_a.get(pos)
connect_two_lists(connector, list_b)
print(getIntersectionNode(list_a, list_b).val)
