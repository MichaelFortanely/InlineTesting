# https://github.com/qiyuangong/leetcode/blob/master/python/058_Length_of_Last_Word.py
from inline import Here

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        temp = s.split(' ')
        print(temp)
        temp2 = [t for t in temp if len(t) > 0]
        Here().given(temp, ['    ', 'hello']).check_eq(temp2, ['hello'])

        print(temp)
        if len(temp) == 0:
            return 0
        else:
            return len(temp[-1])

s = Solution()
s.lengthOfLastWord("hell o         my name is")