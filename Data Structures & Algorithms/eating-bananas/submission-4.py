
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        

        #eating rate: pile ceil(size / rate) = time
        #assuming h >= len(piles)
        l, r = 1, max(piles)
        answer = max(piles)

        while l <= r:
            k = l + (r-l)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours <= h:
                answer = min(answer, k)
                r = k - 1
            else:
                l = k + 1
        return answer

        
