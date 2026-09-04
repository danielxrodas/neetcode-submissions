from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        queue = deque([root])

        while queue:
            if not root: return []
            sublist = []

            for i in range(len(queue)):
                root = queue.popleft()
                sublist.append(root.val)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
            
            res.append(sublist)
        
        return res