from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    idx1 = idx2 = 0
    while idx2 < len(nums2):
        if idx1 < m and nums1[idx1] < nums2[idx2]:
            idx1 += 1
        else:
            nums1[idx1 + 1:] = nums1[idx1:-1]
            nums1[idx1] = nums2[idx2]
            idx2 += 1
            m += 1
            idx1 += 1


arr1 = [1, 2, 3, 0, 0, 0]
arr2 = [2, 5, 6]
merge(arr1, 3, arr2, 3)
print(arr1)

arr1 = [0]
arr2 = [1]
merge(arr1, 0, arr2, 1)
print(arr1)

arr1 = [1, 0]
arr2 = [2]
merge(arr1, 1, arr2, 1)
print(arr1)