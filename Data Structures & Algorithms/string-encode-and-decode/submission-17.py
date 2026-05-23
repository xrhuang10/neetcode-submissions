class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ''
        for string in strs:
            answer += str(len(string)) + '#' + string

        return answer

    def decode(self, s: str) -> List[str]:
        answer = []
        l = 0
        while l < len(s): 
            r = l
            while s[r] != '#':
                r += 1

            length = int(s[l:r])

            answer.append(s[r + 1: r + 1 + length])
            l = r + 1 + length
        
        return answer