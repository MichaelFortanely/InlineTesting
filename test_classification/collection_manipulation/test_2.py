import sys
from inline import Here

#Source: NeetCode(3Sum)
#Classification: Two-Pointer

#Example Case
ex = [-1, -1, 2]

class sol:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    check = a + nums[l] + nums[r]
                    Here().given(a, -1).given(nums, [-1, 2]).given(l, 0).given(r, 1).check_true(check == 0)
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

obj = sol()
trio = obj.threeSum(ex)
print(trio)