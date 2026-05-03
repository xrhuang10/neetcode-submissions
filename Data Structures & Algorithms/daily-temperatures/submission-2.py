class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = len(temperatures)*[0]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                ind, t = stack.pop()
                answer[ind] = i - ind
            
            stack.append((i, temp))
        
        return answer