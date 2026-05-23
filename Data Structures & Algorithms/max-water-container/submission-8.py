class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        answer = 0

        while l <= r:
            answer = max(answer, min(heights[l], heights[r]) * (r - l))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return answer
