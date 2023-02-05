# https://github.com/qiyuangong/leetcode/blob/master/python/047_Permutations_II.py

from inline import Here

class Solution(object):
    def permuteUnique(self, nums):
        # iterative solution
        res = [[]]
        for i in range(len(nums)):
            cache = set()
            while len(res[0]) == i:
                curr = res.pop(0)
                for j in range(len(curr) + 1):
                    # generate new n permutations from n -1 permutations
                    new_perm = curr[:j] + [nums[i]] + curr[j:]
                    print(new_perm)
                    stemp = ''.join(map(str, new_perm))
                    print(stemp)
                    if stemp not in cache:
                        cache.add(stemp)
                        res.append(new_perm)
        return res

Solution.permuteUnique("l", '1234')