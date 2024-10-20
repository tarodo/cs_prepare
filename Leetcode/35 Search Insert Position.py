"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        cur = (left + right) >> 1
        if nums[cur] == target:
            return cur
        if target < nums[cur]:
            right = cur - 1
        else:
            left = cur + 1
    return left