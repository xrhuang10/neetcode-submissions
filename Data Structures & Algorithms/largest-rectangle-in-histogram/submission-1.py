class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #indices only
        answer = 0
        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                height = heights[stack.pop()] 
                width = i - stack[-1] - 1 if stack else i
                answer = max(answer, height * width)

            stack.append(i)
        
        return answer
