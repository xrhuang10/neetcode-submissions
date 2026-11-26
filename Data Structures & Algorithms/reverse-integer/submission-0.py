class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        negative = False
        if x[0] == '-':
            negative = True
            x = x[1:]
        x = int(x[::-1])
        if negative:
            x *= -1
        return x if -2**31 <= x < 2**31 else 0

        