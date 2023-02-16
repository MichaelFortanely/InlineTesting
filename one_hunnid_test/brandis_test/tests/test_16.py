from inline import Here
from typing import List

def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    res = 0
    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        # inline test here
        Here().given(res, 0).given(r, 1).given(l, 0).given(height, [2, 4, 3]).check_eq(res, 2)
        if height[l] < height[r]:
            l += 1
        elif height[r] <= height[l]:
            r -= 1
    return res
