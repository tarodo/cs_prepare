from typing import List


def searchRange(nums: list[int], target: int) -> list[int]:
    def findBound(nums: List[int], target: int, is_first: bool) -> int:
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = int((begin + end) / 2)
            if nums[mid] == target:
                if is_first:
                    if mid == begin or nums[mid - 1] < target:
                        return mid
                    end = mid - 1
                else:
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    begin = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return -1

    left = findBound(nums, target, True)
    if left == -1:
        return [-1, -1]

    right = findBound(nums, target, False)

    return [left, right]




nums = [5,7,7,8,8,10]
target = 5
print(searchRange(nums, target))

nums = [5,7,7,8,8,10]
target = 10
print(searchRange(nums, target))

nums = [1]
target = 1
print(searchRange(nums, target))