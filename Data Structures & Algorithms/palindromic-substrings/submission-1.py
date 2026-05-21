class Solution:
    def countSubstrings(self, s: str) -> int:

        answer = ''
        maxlength = 0
        counter = 0
        
        for i in range(len(s)):

            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                counter += 1
                left -= 1
                right += 1

            

            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                counter += 1

                left -= 1
                right += 1


        
        return counter
                


        

        