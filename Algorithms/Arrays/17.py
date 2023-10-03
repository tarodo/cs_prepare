from collections import Counter


def numIdenticalPairs(nums: list[int]) -> int:
    return sum([cnt*(cnt-1)//2 for num, cnt in Counter(nums).items()])

nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))

nums = [1, 1, 1, 1]
print(numIdenticalPairs(nums))
