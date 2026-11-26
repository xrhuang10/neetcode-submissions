class Solution:
    def reverseBits(self, n: int) -> int:

        answer = 0
        for i in range(32):
            exponent = 32 - i - 1
            yes = (1 << i) & n
            if yes:
                answer += 2 ** exponent
        return answer