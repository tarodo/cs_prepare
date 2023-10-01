def find132pattern(nums: list[int]) -> bool:
    if len(nums) < 3:
        return False
    min_nums = [-float("inf")]*len(nums)
    min_nums[0] = nums[0]
    for idx in range(1, len(nums)):
        min_nums[idx] = min(min_nums[idx-1], nums[idx])
    stack = []

    for idx in range(len(nums) - 1, -1, -1):
        if nums[idx] == min_nums[idx]:
            continue
        while stack and stack[-1] <= min_nums[idx]:
            stack.pop()
        if stack and stack[-1] < nums[idx]:
            return True
        stack.append(nums[idx])
    return False


nums = [1,2,3,4]
print(find132pattern(nums))