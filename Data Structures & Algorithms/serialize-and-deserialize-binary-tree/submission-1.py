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
        while r < len(data):
            if data[r] == ',':
                if data[l:r] == '#':
                    treelist.append(None)
                else:
                    treelist.append(int(data[l:r]))
                l = r + 1
            r += 1
        
        if not treelist or treelist[0] is None:
            return None
        
        q = deque()
        root = TreeNode(treelist[0])
        q.append(root)

        i = 1

        while q and i < len(treelist):
            node = q.popleft()
            if treelist[i] is not None:
                node.left = TreeNode(treelist[i])
                q.append(node.left)
            
            i += 1
            if treelist[i] is not None and i < len(treelist):
                node.right = TreeNode(treelist[i])
                q.append(node.right)
            i += 1

        return root
