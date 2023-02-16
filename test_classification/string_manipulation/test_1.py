import sys
from inline import Here

#Source: NeetCode (Minimum Window Substring)
#Classification: Sliding Window

string1 = "abcdefg"
string2 = "abd"

class MWS:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
    
    def check(self, s: str, t: str) -> bool:
        set1 = set(s)
        set2 = set(t)
        
        for c in set2:
            if c not in set1:
                return False
        
        return True
            
mws = MWS()
finder = mws.minWindow(string1, string2)
Here().given(string1, "abcdefg").given(string2, "abf").check_eq(finder, "abcdef")
