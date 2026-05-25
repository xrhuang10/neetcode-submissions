class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        for task in tasks:
            hashmap[task] = 1 + hashmap.get(task, 0)

        maxheap = []
        for task in hashmap:
            maxheap.append(-1 * hashmap[task])

        heapq.heapify(maxheap)

        q = deque()
        time = 0

        while q or maxheap:
            time += 1
            if maxheap:
                cnt = -1 * heapq.heappop(maxheap) - 1 #decrement count
                if cnt:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                addbackcount, addbacktime = q.popleft()
                heapq.heappush(maxheap, -1 * addbackcount)
        
        return time
