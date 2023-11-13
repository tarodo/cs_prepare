from typing import Optional
from base import ListNode, upload_list, print_linked_list


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    super_first = ListNode(-1)
    new_cur = super_first
    add_one = False
    while l1 or l2:
        l1_el = l1.val if l1 else 0
        l2_el = l2.val if l2 else 0
        new_sum = l1_el + l2_el + add_one
        add_one, new_sum = divmod(new_sum, 10)
        new_cur.next = ListNode(new_sum)
        new_cur = new_cur.next
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2

    if add_one:
        new_cur.next = ListNode(1)
    return super_first.next


def addTwoNumbers2(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    super_first = ListNode(-1)
    new_cur = super_first
    add_one = False
    while l1 or l2:
        l1_el = l1.val if l1 else 0
        l2_el = l2.val if l2 else 0
        new_sum = l1_el + l2_el + add_one
        add_one, new_sum = divmod(new_sum, 10)
        if l1:
            l1.val = new_sum
            new_cur.next = l1
        else:
            l2.val = new_sum
            new_cur.next = l2
        new_cur = new_cur.next
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2

    if add_one:
        new_cur.next = ListNode(1)
    return super_first.next


nums1 = upload_list([2, 4, 3])
nums2 = upload_list([5, 6, 4])
new_head = addTwoNumbers2(nums1, nums2)
print_linked_list(new_head)

nums1 = upload_list([9, 9, 9, 9, 9, 9, 9])
nums2 = upload_list([9, 9, 9, 9])
new_head = addTwoNumbers2(nums1, nums2)
print_linked_list(new_head)

nums1 = upload_list([0])
nums2 = upload_list([0])
new_head = addTwoNumbers2(nums1, nums2)
print_linked_list(new_head)
