# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        code = ''
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                code += '#'
            else:
                code += str(node.val)
                q.append(node.left)
                q.append(node.right)
            code += ','
            

        print(code)
        return code

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        l, r = 0, 0
        treelist = []
        for r in range(len(data)):
            if data[r] != ',':
                continue
            value = data[l:r]
            if value == '#':
                treelist.append(None)
            else:
                treelist.append(int(data[l:r]))
            l = r + 1

        if not treelist or treelist[0] == None:
            return None
        head = builderNode = TreeNode(treelist[0])
        q = deque()
        q.append((builderNode))
        i = 1
        while q and i < len(data):
            node = q.popleft()
            if treelist[i] is not None:
                node.left = TreeNode(treelist[i])
                q.append(node.left)
            i += 1
            if treelist[i] is not None:
                node.right = TreeNode(treelist[i])
                q.append(node.right)
            i += 1
        return head
            


        

