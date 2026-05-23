class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = len(temperatures) * [0]
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index, temperature = stack.pop()
                output[index] = i - index
            stack.append((i, temp))
        
        return output