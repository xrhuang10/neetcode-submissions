# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[0, root]]
        res = 0
        depth = 0
        while stack:
            depth, node = stack.pop()

            if node:
                depth += 1
                stack.append([depth, node.left])
                stack.append([depth, node.right])
            res = max(res, depth)
            
            
            
        return res
        

