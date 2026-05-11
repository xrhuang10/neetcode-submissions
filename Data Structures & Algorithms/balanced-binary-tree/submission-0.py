# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.answer = True
        def dfs(node):
            if not node:
                return 0
            
            leftmax = dfs(node.left)
            rightmax = dfs(node.right)

            if abs(rightmax - leftmax) > 1:
                self.answer = False

            return 1 + max(leftmax, rightmax)
            
        dfs(root)
        return self.answer