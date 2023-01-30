from inline import Here
from typing import List

def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
    m = len(rolls)
    curSum = sum(rolls)
    missingSum = mean * (n + m) - curSum
    # inline test here
    Here().given(mean, 3).given(m, 4).given(n, 1).given(curSum, 0).check_eq(missingSum, 15)
    if missingSum < n or missingSum > 6*n: return []

    part, rem = divmod(missingSum, n)
    ans = [part] * n
    for i in range(rem):
        ans[i] += 1
    return ans