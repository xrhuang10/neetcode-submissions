class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        for i in range(len(position)):
            fleet.append((position[i], speed[i]))
        
        fleet.sort()
        print(fleet)

        stack = []
        for carpos, carspeed in fleet:
            time = (target - carpos)/carspeed
            while stack and time >= (target - stack[-1][0])/stack[-1][1]:
                stack.pop()

            stack.append((carpos, carspeed))
        
        return len(stack)
            

            
