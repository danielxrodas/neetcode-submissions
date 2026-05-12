# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        elif not subRoot:
            return True

        def isSameTree(p, q):
            if not p and not q: 
                return True
            if not p and q or not q and p or p.val != q.val or not isSameTree(p.left, q.left) or not isSameTree(p.right, q.right):
                return False
            return True
            
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
