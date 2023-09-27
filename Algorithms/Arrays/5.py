from typing import List


def checkIfExist(arr: List[int]) -> bool:
    for i_idx, i in enumerate(arr):
        for j_idx, j in enumerate(arr):
            if i_idx != j_idx and i == 2 * j:
                print(i, j)
                return True
    return False


print(checkIfExist([-2,0,10,-19,4,6,-8]))