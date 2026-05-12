# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = preorder[0]
        mid = inorder.index(root)

        head = TreeNode(root)

        leftsubtree = inorder[0:mid]
        rightsubtree = inorder[mid + 1:]

        head.left = self.buildTree(preorder[1:1 + len(leftsubtree)], leftsubtree)
        head.right = self.buildTree(preorder[1 + len(leftsubtree):], rightsubtree)

        return head
        
        