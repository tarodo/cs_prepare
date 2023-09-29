from typing import List


def isMonotonic(nums: List[int]) -> bool:
    return all(nums[idx] >= nums[idx + 1] for idx in range(len(nums) - 1)) or all(nums[idx] <= nums[idx + 1] for idx in range(len(nums) - 1))


nums = [1,2,2,3]
print(isMonotonic(nums))
nums = [6,5,4,4]
print(isMonotonic(nums))
nums = [1,3,2]
print(isMonotonic(nums))
nums = [1, 1, 1]
print(isMonotonic(nums))
