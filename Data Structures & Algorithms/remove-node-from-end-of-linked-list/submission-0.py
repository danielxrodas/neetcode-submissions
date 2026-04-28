# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Brute force 
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        curr = head
        node_list = []

        while curr:
            node_list.append(curr)
            curr = curr.next

        node_to_delete = len(node_list) - n

        if node_to_delete == 0:
            return head.next

        node_list[node_to_delete - 1].next = node_list[node_to_delete].next

        return head