
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        

        #eating rate: pile ceil(size / rate) = time
        l, r = 1, max(piles)
        answer = max(piles)
        while l <= r:
            k = l + (r-l)//2
            count = 0
            for pile in piles:
                count += math.ceil(pile / k) 

            if count <= h:
                answer = min(answer, k)
                r = k - 1
            elif count > h:
                l = k + 1

        return answer

        
