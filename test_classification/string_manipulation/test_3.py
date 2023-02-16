import sys
from inline import Here

#Source: NeetCode (Valid Parenthesis Problem)
#Classification: Stack

#Example Case
brackets = "[][][][[[]]]{}}"

class Valid_Parenthesis:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack

valid_parenthesis = Valid_Parenthesis()
answer = valid_parenthesis.isValid(brackets)
Here().given(brackets, '[[]][]{}()').check_eq(answer, True)
