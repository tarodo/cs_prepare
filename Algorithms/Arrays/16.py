def findDisappearedNumbers(nums: list[int]) -> list[int]:
    set_1 = {el for el in range(1, len(nums)+1)}
    set_2 = set(nums)
    return list(set_1 - set_2)


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))
nums = [1, 1]
print(findDisappearedNumbers(nums))
nums = [1]
print(findDisappearedNumbers(nums))
