# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Optimal Solution
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        left = head
        right = head

        for i in range(n+1):
            if right == None:
                return head.next
            right = right.next

        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return head
