from typing import List


def removeElement(nums: List[int], val: int) -> int:
    new_idx = 0
    for idx, num in enumerate(nums):
        if num != val:
            nums[new_idx] = num
            new_idx += 1
    return new_idx


result = removeElement([3, 2, 2, 3], 3)
print(result)
