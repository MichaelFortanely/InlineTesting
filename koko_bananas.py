from typing import List
from inline import Here
import math

def minEatingSpeed(self, piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    res = max(piles)
    while l <= r:
        k = (l + r) // 2
        totalTime = 0
        for p in piles:
            totalTime += math.ceil(p / k)
            # inline test here
            Here().given(totalTime, 3).given(p, 5).given(k, 3).check_eq(totalTime, 5)
        if totalTime <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res