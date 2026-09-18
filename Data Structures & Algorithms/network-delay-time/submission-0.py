class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = deque()

        adj = defaultdict(list)
        maptimes = {}
        for i in range(len(times)):
            ui = times[i][0]
            vi = times[i][1]
            ti = times[i][2]
            adj[ui].append((vi, ti))

        maptimes = {i: float("inf") for i in range(1, n+1)}
        maptimes[k] = 0

        q.append((k, 0))

        while q:
            node, time = q.popleft()
            if maptimes[node] < time:
                continue
            neighbors = adj[node]
            for neighbor, addtime in neighbors:
                if time + addtime < maptimes[neighbor]:
                    maptimes[neighbor] = time + addtime
                    q.append((neighbor, time + addtime))
        
        res = max(maptimes.values())

        return res if res < float("inf") else -1

