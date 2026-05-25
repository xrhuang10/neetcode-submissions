class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heap.append(((point[0]**2 + point[1]**2)**0.5, point))
        
        heapq.heapify(heap)
        answer = []
        for i in range(k):
            distance, point = heapq.heappop(heap)
            answer.append(point)
        
        return answer

