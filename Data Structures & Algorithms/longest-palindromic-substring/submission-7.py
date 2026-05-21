class Solution:
    def longestPalindrome(self, s: str) -> str:

        answer = ''
        maxlength = 0
        
        for i in range(len(s)):

            left, right = i, i
            word = s[left:right + 1]
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(word) > maxlength:
                    answer = word
                    maxlength = len(word)
                word = s[left-1:right+2]
                left -= 1
                right += 1

            

            left, right = i, i + 1
            word = s[left:right+1]
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(word) > maxlength:
                    answer = word
                    maxlength = len(word)
                word = s[left-1:right+2]
                left -= 1
                right += 1


        
        return answer
                


        
