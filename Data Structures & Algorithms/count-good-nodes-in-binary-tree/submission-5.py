# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0

        def dfs(node, maxparentval):
            if not node:
                return 

            if maxparentval <= node.val:
                self.counter += 1
                maxparentval = node.val

            dfs(node.left, maxparentval)
            dfs(node.right, maxparentval)
            return 
        
        dfs(root, root.val)

        return self.counter

                

                

        