 # https://github.com/qiyuangong/leetcode/blob/master/python/071_Simplify_Path.py

from inline import Here

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = []
        plist = path.split('/')
        for pos in plist:
            if pos:
                if pos == '..':
                    try:
                        # up one level
                        result.pop()
                    except:
                        # arrive top level
                        result = []
                elif pos != '.':
                    result.append(pos)
        print(result)
        result2 = '/'+'/'.join(result)
        Here().given(result, ['he', '4', 'ddd']).check_eq(result2, '/he/4/1/65d')
        Here().given(result, ['he', '  ', '5']).check_eq(result2, '/he/  /5')

        return result2

print(Solution.simplifyPath("s", "he/4/  //1/./65d"))