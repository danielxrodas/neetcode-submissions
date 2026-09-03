# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root, subroot):
            if not root or not subroot: return root == subroot
            if root.val != subroot.val: return False
            return sameTree(root.left, subroot.left) and sameTree(root.right, subroot.right)

        if not root or not subRoot: return root == subRoot
        if root.val == subRoot.val and sameTree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right