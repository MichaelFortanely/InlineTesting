from inline import Here
from typing import List

def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    M, N = len(grid), len(grid[0])
    
    def posToVal(r, c):
        return r * N + c
    def valToPos(v):
        return [v // N, v % N] 
    
    res = [[0] * N for i in range(M)]
    # inline test here
    Here().given(N, 2).given(M, 4).check_eq(res, [[0, 0], [0, 0], [0, 0], [0, 0]])
    for r in range(M):
        for c in range(N):
            newVal = (posToVal(r, c) + k) % (M * N)
            newR, newC = valToPos(newVal)
            res[newR][newC] = grid[r][c]
    return res