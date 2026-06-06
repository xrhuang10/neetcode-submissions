class Solution:
    def hammingWeight(self, n: int) -> int:
        answer =0 
        while n != 0:
            bit = n%2
            n = n//2
            if bit == 1:
                answer += 1

        return answer