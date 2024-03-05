# Problem Link: https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends
# Daily Question - March 5, 2025

class Solution:
    def minimumLength(self, s: str) -> int:
        lo, hi = 0, len(s) - 1

        while lo < hi and s[lo] == s[hi]:
            currChar = s[lo]
            
            while lo <= hi:
                if s[lo] != currChar:
                    break
                lo += 1

            while lo <= hi:
                if s[hi] != currChar:
                    break
                hi -= 1
        
        return hi  - (lo - 1)
