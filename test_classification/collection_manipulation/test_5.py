import sys
from inline import Here

#Source: NeetCode(Linked List Cycle)
#Classification: LinkedLists

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#Example Case:
Root = ListNode(1)
Root.next = ListNode(2)
Root.next.next = Root

Root2 = ListNode(1)
Root2.next = ListNode(2)
Root2.next.next = ListNode(3)

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                x = slow
                Here().given(slow, ListNode(1)).given(fast, slow).check_eq(x, fast)
                return True
        return False
    
obj = Solution()
