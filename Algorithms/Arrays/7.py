from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    cur_idx = 0
    for idx, el in enumerate(nums):
        if el:
            nums[cur_idx] = el
            cur_idx += 1
    nums[cur_idx:] = [0] * (len(nums) - cur_idx)



nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)
nums = [0]
moveZeroes(nums)
print(nums)
nums = [1, 2, 3]
moveZeroes(nums)
print(nums)