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
        leftsubtree = inorder[:mid]
        rightsubtree = inorder[mid + 1:]

        head = builderNode = TreeNode(root)

        builderNode.left = self.buildTree(preorder[1:], leftsubtree)
        builderNode.right = self.buildTree(preorder[1 + len(leftsubtree):], rightsubtree)

        return head

        
        