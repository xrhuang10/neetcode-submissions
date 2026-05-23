class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        processed = ''
        for char in s:
            if char.isalnum():
                processed += char
        processed = processed.lower()
        l, r = 0, len(processed) - 1
        while l <= r:
            if processed[l] != processed[r]:
                return False
            l += 1
            r -= 1
        
        return True