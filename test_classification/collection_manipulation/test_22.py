# https://github.com/qiyuangong/leetcode/blob/master/python/038_Count_and_Say.py
from inline import Here

class Solution:

    def count(self, x):
        m = list(x)
        print(m)
        res = []
        m.append(None)
        test = m[len(m) - 1]
        Here().check_same(test, None)
        
        print(m)
        i , j = 0 , 0
        while i < len(m) - 1:
            j += 1
            if m[j] != m[i]:
                # note j - i is the count of m[i]
                res += [j - i, m[i]]
                i = j
        return ''.join(str(s) for s in res)

Solution.count("l", '543')