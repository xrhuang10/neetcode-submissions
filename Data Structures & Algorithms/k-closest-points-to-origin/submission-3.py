class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point[0], point[1]
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (distance, x, y))

        answer = []
        
        for i in range(k):
            distance, x, y = heapq.heappop(heap)
            answer.append([x, y])
        
        return answer

        

