class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #index, height
        answer = 0
        for i, h in enumerate(heights):
            newindex = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                answer = max(answer, height * (i - index))
                newindex = index
            stack.append((newindex, h))
        
        for start, h in stack:
            answer = max(answer, h * (len(heights) - start))
        
        return answer
