# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        result = [root.val]

        def dfs(root):
            if not root: return 0

            lhs = dfs(root.left)
            rhs = dfs(root.right)
            lhs = max(lhs, 0)
            rhs = max(rhs,0)

            result[0] = max(result[0], root.val + lhs + rhs)

            return max(root.val, root.val + max(lhs,rhs))

        dfs(root)

        return result[0]