# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        answer = ''
        
        q = deque()
        q.append(root)
        while q:


            for i in range(len(q)):
                node = q.popleft()
                if node:
                    answer += str(node.val)
                    answer += ','
                    q.append(node.left)
                    q.append(node.right)

                else:
                    answer += '#'
                    answer += ','



        
        print(answer)
        return answer
                

                

        


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        l, r = 0, 0
        treelist = []


        while r != len(data):

            if data[r] == ',':
                nodeval = None if data[l:r] == '#' else int(data[l:r]) 
                treelist.append(nodeval)
                l = r + 1
            r += 1
        
        print(treelist)
        if not treelist or treelist[0] is None:
            return None

        root = TreeNode(treelist[0])
        q = deque([root])
        i = 1
        while q and i < len(treelist):
            node = q.popleft()

            if treelist[i] is not None:
                node.left = TreeNode(treelist[i])
                q.append(node.left)
            i += 1

            if i < len(treelist) and treelist[i] is not None:
                node.right = TreeNode(treelist[i])
                q.append(node.right)
            i += 1
                
            

        return root
