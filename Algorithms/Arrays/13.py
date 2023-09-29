from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    max_1 = cur_1 = next_1 = 0
    for el in nums:
        if el == 1:
            cur_1 += 1
            next_1 += 1
        else:
            max_1 = max(cur_1, max_1)
            cur_1 = next_1 + 1
            next_1 = 0
    max_1 = max(cur_1, max_1)
    return max_1



nums = [1, 0, 1, 1, 0]
print(findMaxConsecutiveOnes(nums))

nums = [1, 0, 1, 1, 0, 1]
print(findMaxConsecutiveOnes(nums))

nums = [1,1,0,1]
print(findMaxConsecutiveOnes(nums))
