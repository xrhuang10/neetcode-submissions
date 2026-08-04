class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        for i in range(k):
            answer = heapq.heappop(nums)
        
        return -1 * answer