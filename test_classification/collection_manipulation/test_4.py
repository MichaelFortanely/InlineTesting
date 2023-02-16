import math
import sys
from inline import Here

#Source: NeetCode(Koko Eating Bananas)
#Classification: Binary Search

#Example Case:
case = [2, 3, 7, 11]

class bananas:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
    
solution = bananas()
time = 8
rate = solution.minEatingSpeed(case, time)
Here().given(case, [3, 6, 9, 12]).given(time, 6).check_eq(rate, 6)
