# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root or not subRoot: return root == subRoot
        if root.val != subRoot.val: return False

        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
