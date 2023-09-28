from typing import List


def heightChecker(heights: List[int]) -> int:
    return sum([not h1 == h2 for h1, h2 in zip(heights, sorted(heights))])


heights = [1,1,4,2,1,3]
print(heightChecker(heights))