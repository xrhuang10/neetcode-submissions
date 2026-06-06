class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            answer = 0
            while num != 0:
                bit = num%2
                num = num//2
                if bit == 1:
                    answer += 1
            res.append(answer)
        
        return res