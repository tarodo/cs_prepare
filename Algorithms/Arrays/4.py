from typing import List


def replaceElements(arr: List[int]) -> List[int]:
    cur_max = -1
    for idx in range(len(arr) - 1, -1, -1):
        arr[idx], cur_max = cur_max, max(arr[idx], cur_max)
    return arr


arr = [17,18,5,4,6,1]
arr = replaceElements(arr)
print(arr)