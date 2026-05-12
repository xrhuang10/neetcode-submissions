# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #make one satck per level, append to stack from l to r, pop the top, then reset to 0
        #BFS
        answer = []
        if not root:
            return []
        
        q = deque()
        q.append(root)

        while q:
            rightside = None
            for i in range(len(q)):
                levelelement = q.popleft()
                
                if levelelement:
                    q.append(levelelement.left) 
                    q.append(levelelement.right) 
                    rightside = levelelement
            if rightside:
                answer.append(rightside.val)
            
        return answer
                


