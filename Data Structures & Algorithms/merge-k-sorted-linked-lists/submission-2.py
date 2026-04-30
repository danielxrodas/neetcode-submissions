# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Optimal
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

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


        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(mergetwolists(l1,l2))
            
            lists = merged
        
        return lists[0]
