from typing import Optional
from base import ListNode, upload_list, print_linked_list


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    super_first = ListNode(-1)
    new_cur = super_first
    while list1 and list2:
        if list1.val > list2.val:
            new_cur.next = list2
            list2 = list2.next
        else:
            new_cur.next = list1
            list1 = list1.next
        new_cur = new_cur.next

    new_cur.next = list1 or list2
    return super_first.next


nums1 = upload_list([1, 2, 4])
nums2 = upload_list([1, 3, 4])
new_head = mergeTwoLists(nums1, nums2)
print_linked_list(new_head)

nums1 = upload_list([])
nums2 = upload_list([])
new_head = mergeTwoLists(nums1, nums2)
print_linked_list(new_head)

nums1 = upload_list([])
nums2 = upload_list([0])
new_head = mergeTwoLists(nums1, nums2)
print_linked_list(new_head)