# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr: 
            next_node = curr.next
            curr.next = prev
            prev = curr 
            curr = next_node
        
        pointer1 = head
        pointer2 = prev

        while pointer1 and pointer2:
            first_next = pointer1.next
            second_next = pointer2.next
            pointer1.next = pointer2
            pointer2.next = first_next
            pointer1 = first_next
            pointer2 = second_next
