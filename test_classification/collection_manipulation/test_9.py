import sys
from inline import Here

#Source: NeetCode (kth Smallest element in BST)
#Classification: Trees

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Example Case
root = TreeNode(5)
root.left = TreeNode(10)
root.right = TreeNode(15)
        
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            prev_val = curr.val
            curr = curr.right
            Here().given(curr, TreeNode(5)).given(curr.right, TreeNode(3)).check_eq(curr.val, 3)

solution = Solution()
r = root
answer = solution.kthSmallest(r, 1)
