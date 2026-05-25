class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        counter = 0

        adj = {i:[] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            if visited[node] == True:
                return None
            
            visited[node] = True

            neighbors = adj[node]

            for nei in neighbors:
                dfs(nei)
            
            return None


        for i in range(n):
            if visited[i] == False:
                counter += 1
                dfs(i)
        
        return counter
