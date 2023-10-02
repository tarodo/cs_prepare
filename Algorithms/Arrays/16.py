def findDisappearedNumbers(nums: list[int]) -> list[int]:
    set_2 = set(nums)
    result = []
    for el in range(1, len(nums) + 1):
        if el not in set_2:
            result.append(el)
    return result


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))
nums = [1, 1]
print(findDisappearedNumbers(nums))
nums = [1]
print(findDisappearedNumbers(nums))
