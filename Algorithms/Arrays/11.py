from typing import List


def isMonotonic(nums: List[int]) -> bool:
    inc = None
    for idx in range(len(nums) - 1):
        if inc is None:
            if nums[idx] > nums[idx + 1]:
                inc = False
            if nums[idx] < nums[idx + 1]:
                inc = True
        else:
            if nums[idx] > nums[idx + 1] and inc:
                return False
            if nums[idx] < nums[idx + 1] and not inc:
                return False
    return True


nums = [1,2,2,3]
print(isMonotonic(nums))
nums = [6,5,4,4]
print(isMonotonic(nums))
nums = [1,3,2]
print(isMonotonic(nums))
nums = [1, 1, 1]
print(isMonotonic(nums))
