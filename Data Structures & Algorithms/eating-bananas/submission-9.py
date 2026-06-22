
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        answer = max(piles)

        while l <= r:
            k = l + (r-l)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours > h:
                l = k + 1
            else:
                r = k - 1
                answer = min(answer, k)

            
        return answer

        

            


        
