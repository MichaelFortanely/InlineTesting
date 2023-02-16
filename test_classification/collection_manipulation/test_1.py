import sys
from inline import Here

#Source: Tyler Ferrari
#Classification: Arrays/Hashing

#Example Case
nums = [1, 2, 3, 4, 5, 10, 1]
nums2 = [1, 2, 3, 4, 5, 10]

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        repeat = set()

        for n in nums:
            if n in nums:
                return True
            repeat.add(n)

        return False
    
solution = Solution()
answer = solution.containsDuplicate(nums)
Here().given(nums, [1,2,3]).check_eq(answer, True)
