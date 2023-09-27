from typing import List


def validMountainArray(arr: List[int]) -> bool:
    if len(arr) <= 1:
        return False
    if arr[0] >= arr[1]:
        return False
    pos = True
    for idx in range(1, len(arr)):
        if arr[idx-1] == arr[idx]:
            return False
        if pos:
            if arr[idx-1] > arr[idx]:
                pos = False
        else:
            if arr[idx-1] < arr[idx]:
                return False
    return not pos
