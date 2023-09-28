from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] % 2 > nums[j] % 2:
            nums[i], nums[j] = nums[j], nums[i]

        if not nums[i] % 2: i += 1
        if nums[j] % 2: j -= 1
    return nums

nums = [3, 1, 2, 4]
sortArrayByParity(nums)
print(nums)