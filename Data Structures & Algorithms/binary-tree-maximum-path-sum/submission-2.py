# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.globalmax = float("-infinity")

        def dfs(node): #returns the max path if we split
            if not node:
                return 0

            leftmax = max(dfs(node.left), 0)
            rightmax = max(dfs(node.right), 0)
            currentsum = leftmax + node.val + rightmax
            self.globalmax = max(self.globalmax, currentsum)

            return node.val + max(leftmax, rightmax)
        
        dfs(root)

        return self.globalmax
            