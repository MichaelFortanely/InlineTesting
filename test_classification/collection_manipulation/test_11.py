import sys
from inline import Here

#Source: NeetCode(JumpGame)
#Classification: Greedy

example = [1, 2, 0, 0, 3]
example2 = [1, 3, 0, 0, 3]

class JumpGame:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
    
Jumper = JumpGame()
Boolean = Jumper.canJump(example)
Here().given(example, [1, 2, 3]).check_eq(Boolean, True)

print(Boolean)
