class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        print(adj)

        def dfs(node):

            
            visited[node] = True

            neighbors = adj[node]

            for nei in neighbors:
                if not visited[nei]:
                    
                    dfs(nei)
            
        
        counter = 0
        for i in range(n):
            if visited[i] == False:
                dfs(i)
                counter += 1
        return counter