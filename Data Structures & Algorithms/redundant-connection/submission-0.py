class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        seen = set()
        adj = {i:[] for i in range(1, len(edges) + 1)}

        def checkCycle(src, target, visited):
            if src == target:
                return True
            visited.add(src)
            for nei in adj[src]:
                if nei not in visited:
                    if checkCycle(nei, target, visited):
                        return True
            return False

        for u, v in edges:
            if checkCycle(u, v, set()):
                return [u, v]
            adj[u].append(v)
            adj[v].append(u)
            