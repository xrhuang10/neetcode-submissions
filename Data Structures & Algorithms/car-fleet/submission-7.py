class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuples = []
        n = len(position)
        
        for i in range(n):
            tuples.append((position[i], speed[i]))
        tuples.sort()
        
        times = []
        for j in range(n):
            times.append((target - tuples[j][0])/tuples[j][1])

        stack = []
        for t in times:
            while stack and t >= stack[-1]:
                stack.pop()
            stack.append(t)
            
    
        return len(stack)
            
