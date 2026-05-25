class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = {i:[] for i in range(1, len(edges) + 1)}


        def dfs(node, target, seen):
            if node == target:
                return True

            seen.add(node)

            neighbors = adj[node]

            for nei in neighbors:
                if nei not in seen:
                    if dfs(nei, target, seen) == True:
                        return True
            
            return False
        
        for u, v in edges:
            if dfs(u, v, set()):
                return [u, v]

            adj[u].append(v)
            adj[v].append(u)


            
            
            

            