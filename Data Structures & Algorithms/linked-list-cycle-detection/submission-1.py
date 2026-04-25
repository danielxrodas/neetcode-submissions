# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        stored_nodes = set()
        turtoise = head
        hare = head

        while hare and hare.next:
            turtoise = turtoise.next
            hare = hare.next.next

            if turtoise == hare:
                return True
        
        return False

