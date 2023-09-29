from typing import List


def thirdMax(nums: List[int]) -> int:
    max_list = []
    elms = set()
    for el in nums:
        if el in elms:
            continue
        elms.add(el)
        max_list.append(el)
        max_list.sort()
        max_list = max_list[-3:]
    if len(elms) >= 3:
        return max_list[0]
    return max_list[-1]

nums = [2,2,3,1]
print(thirdMax(nums))

nums = [1,2]
print(thirdMax(nums))