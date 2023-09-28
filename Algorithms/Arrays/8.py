from typing import List


def sortArrayByParity(nums: List[int]) -> List[int]:
    return [el for el in nums if not el % 2] + [el for el in nums if el % 2]


nums = [3, 1, 2, 4]
sortArrayByParity(nums)