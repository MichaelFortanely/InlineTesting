import sys
from inline import Here

#Source: NeetCode(Sum of Two Integers)
#Classfication: Bit Manipulation

#Example Case
a = 4
b = -6

class Combining:
    def getSum(self, a: int, b: int) -> int:
        def add(a, b):
            if not a or not b:
                return a or b
            return add(a ^ b, (a & b) << 1)

        if a * b < 0:  # assume a < 0, b > 0
            if a > 0:
                positive = self.getSum(b, a)
                return positive
            if add(~a, 1) == b:  # -a == b
                zero = 0
                Here().given(a, -1).given(b, 1).check_true(a + b == zero)
                return 0
            if add(~a, 1) < b:  # -a < b
                return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)
               
                
        return add(a, b)  # a*b >= 0 or (-a) > b > 0
    
combine = Combining()
c = combine.getSum(a, b)
