# https://github.com/qiyuangong/leetcode/blob/master/python/029_Divide_Two_Integers.py

import math
from inline import Here

MAX_INT = 50

class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 0:
            return MAX_INT
        if dividend == 0:
            return 0
        isPositive = (dividend < 0) == (divisor < 0)
        print(isPositive)
        Here().given(dividend, 5).given(divisor, 3).check_true(isPositive)
        Here().given(dividend, 3).given(divisor, -5).check_false(isPositive)
        
        m = abs(dividend)
        n = abs(divisor)
        # ln and exp
        res = math.log(m) - math.log(n)
        res = int(math.exp(res))
        if isPositive:
            return min(res, 2147483647)
        return max(0 - res, -2147483648)

Solution.divide("s", 5, 3)