# Problem Link: https://leetcode.com/problems/score-of-a-string
## June 1, 2024

class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        prevCharVal = int(ord(s[0]))
        
        for char in s:
            charVal = int(ord(char))
            res += abs(charVal - prevCharVal)

            prevCharVal = charVal

        return res
