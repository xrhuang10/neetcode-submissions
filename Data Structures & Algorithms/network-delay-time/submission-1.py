class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = deque()
        maptimes = {i:float("inf") for i in range(1, n+1)}
        adj = defaultdict(list)
        for ui, vi, ti in times:
            adj[ui].append((vi, ti)) 

        maptimes[k] = 0
        q.append((k, 0))

        while q:
            node, time = q.popleft()
            if maptimes[node] < time:
                continue
            neighbors = adj[node]
            for nei, addtime in neighbors:
                if time + addtime < maptimes[nei]:
                    maptimes[nei] = time + addtime
                    q.append((nei, time + addtime))
        
        res = max(maptimes.values())
        return res if res < float("inf") else -1
