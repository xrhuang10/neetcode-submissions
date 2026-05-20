class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        cycle = set()
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        print(adj)

        def dfs(node):
            if node in cycle:
                return False
            
            cycle.add(node)

            neighbors = adj[node]

            for nei in neighbors:
                adj[nei].remove(node)
                if not dfs(nei):
                    return False
            
            return True
        
        return dfs(0) and len(cycle) == n

            