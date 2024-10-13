"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.



Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]


Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
"""
from typing import List

test_data = [
    ([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6], [2,2,2,1,4,3,3,9,6,7,19]),
    ([28,6,22,8,44,17], [22,28,8,6], [22,28,8,6,17,44])
]


def relativeSortArray1(arr1: List[int], arr2: List[int]) -> List[int]:
    result = [0] * 1001
    res = []
    for el in arr1:
        result[el] += 1
    for el in arr2:
        res.extend([el] * result[el])
        result[el] = 0
    res.extend([idx for idx, el in enumerate(result) for _ in range(el)])
    return res

def relativeSortArray2(arr1: List[int], arr2: List[int]) -> List[int]:
    from collections import Counter
    counter = Counter(arr1)
    result = []
    for el in arr2:
        if el in counter:
            result.extend([el,]*counter[el])
        del(counter[el])

    result.extend([el for el in sorted(counter.keys()) for _ in range(counter[el])])
    return result


for data in test_data:
    result = relativeSortArray1(data[0], data[1])
    print(f"arr1 = {data[0]}, arr2 = {data[1]} => relativeSortArray = {result} : Result = {result == data[2]}")
    result = relativeSortArray2(data[0], data[1])
    print(f"arr1 = {data[0]}, arr2 = {data[1]} => relativeSortArray2 = {result} : Result = {result == data[2]}")