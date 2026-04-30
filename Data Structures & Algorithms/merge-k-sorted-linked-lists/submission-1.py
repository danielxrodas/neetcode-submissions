# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Brute Force
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        result = lists[0]

        def mergetwolists(l1, l2):

            dummy = ListNode(0)
            curr = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    curr = curr.next
                    l1 = l1.next
                else:
                    curr.next = l2
                    curr = curr.next
                    l2 = l2.next

            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2

            return dummy.next

        for i in range(1, len(lists)):
            result = mergetwolists(result, lists[i])

        return result
