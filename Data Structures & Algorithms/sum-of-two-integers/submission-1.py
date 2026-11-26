class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        answer = 0
        for i in range(32):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1
            currbit = abit ^ bbit ^ carry
            answer += currbit * (2 ** i)
            if abit + bbit + carry > 1:
                carry = 1
            else:
                carry = 0
        return answer if answer < 2**31 else answer - 2**32

            
