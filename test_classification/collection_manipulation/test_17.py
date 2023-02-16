from inline import Here
from typing import List

def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        # inline test here
        Here().given(position, [1, 2, 3]).given(speed, [1, 2]).check_eq(pair, [(1, 1), (2, 2)])
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
