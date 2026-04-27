# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        node_values = []

        while curr:
            node_values.append(curr)
            curr = curr.next
        
        l = 0
        r = len(node_values) - 1

        while l <= r:
            if r == l or r - l == 1:
                break
            node_values[l].next = node_values[r]
            node_values[r].next = node_values[l + 1]
            l += 1
            r -= 1
        
        node_values[r].next = None
