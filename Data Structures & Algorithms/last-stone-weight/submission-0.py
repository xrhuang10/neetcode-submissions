class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        
        while len(stones) > 1:
            heapq.heapify(stones)
            first = -1 * heapq.heappop(stones)
            heapq.heapify(stones)
            second = -1 * heapq.heappop(stones)
            if first > second:
                heapq.heappush(stones, -1 * (first - second))
            
        return -1 * stones[0] if stones else 0
            
        
            