from typing import List


def duplicateZeros(arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    idx = 0
    while idx < len(arr) - 1:
        if not arr[idx]:
            arr[idx + 2:] = arr[idx + 1:-1]
            arr[idx + 1] = 0
            idx += 2
        else:
            idx += 1


arr = [0, 4, 1, 0, 0, 8, 0, 0, 3]
duplicateZeros(arr)

print(arr)
