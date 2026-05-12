# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if not root:
            return []
        
        q = collections.deque()
        q.append(root)

        while q:
            levellist = []
            for i in range(len(q)):
                levelelement = q.popleft()
                
                if levelelement:
                    q.append(levelelement.left) 
                    q.append(levelelement.right) 
                    levellist.append(levelelement.val)
            if levellist:
                answer.append(levellist)
            
        return answer
