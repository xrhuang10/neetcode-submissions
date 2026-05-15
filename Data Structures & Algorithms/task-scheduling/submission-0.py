class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        for task in tasks:
            hashmap[task] = 1 + hashmap.get(task, 0)
        
        maxHeap = [- hashmap[task] for task in hashmap]

        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while q or maxHeap:
            time += 1
            if maxHeap:
                cnt = -1 * heapq.heappop(maxHeap) - 1
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                addbackcount, addbacktime = q.popleft()
                heapq.heappush(maxHeap, -1 * addbackcount)
            
            


        return time