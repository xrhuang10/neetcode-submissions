class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n > 0:
            size = n & -n
            while size > n:
                size //= 2
            answer += 1
            n -= size
        return answer