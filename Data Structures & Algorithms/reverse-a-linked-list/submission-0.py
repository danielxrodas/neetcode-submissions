# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1. Describe the problem:
            Given a singly linked list, they want us to reverse it

        2. Identify the pattern
            Linked List

        3. Steps
        '''
        prev, curr = None, head

        while curr:
            dummy = curr.next  # save next node
            curr.next = prev   # reverse pointer
            prev = curr        # move prev forward
            curr = dummy       # move curr forward

        return prev  # prev is the new head