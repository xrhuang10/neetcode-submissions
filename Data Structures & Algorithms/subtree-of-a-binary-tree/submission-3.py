# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:

      

        def sametree(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2 and root1.val == root2.val:
                return sametree(root1.left, root2.left) and sametree(root1.right, root2.right)
            else:
                return False

        if not root:
            return False
        



        left = self.isSubtree(root.left, subroot)
        right = self.isSubtree(root.right, subroot)
        return left or right or sametree(root, subroot)
