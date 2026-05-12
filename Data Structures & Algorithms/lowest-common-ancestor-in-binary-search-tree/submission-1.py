# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        currentValue = root.val

        if p.val <= currentValue and q.val >= currentValue or p.val >= currentValue and q.val <= currentValue:
            #split happens current root is ancestor
            return root
        
        if p.val < currentValue and q.val < currentValue:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q) 

            