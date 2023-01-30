from inline import Here
from typing import List

def partition(self, s: str) -> List[List[str]]:
    res, part = [], []
    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            if self.isPali(s, i, j):
                part.append(s[i : j + 1])
                # inline test here
                Here().given(part, []).given(s, "banana").given(i, 0).given(j, 1).check_eq(part, ["ba"])
                dfs(j + 1)
                part.pop()
    dfs(0)
    return res
    
def isPali(self, s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True