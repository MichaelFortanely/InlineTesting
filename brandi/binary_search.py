from inline import Here
from typing import List

def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)
        # inline test here
        Here().given(l, 2).given(r, 4).check_eq(m, 3)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1




