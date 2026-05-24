class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maximum = 0

        for i in range(len(heights) + 1):
            start = i
            while stack and (i == len(heights) or heights[i] < stack[-1][1]):
                index, maxheight = stack.pop()
                maximum = max(maximum, maxheight * (i - index))
                start = index

            stack.append((start, heights[i] if i < len(heights) else 1110))
            
            

            
        
        return maximum

