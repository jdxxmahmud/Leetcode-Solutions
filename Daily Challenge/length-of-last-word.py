# Problem Link: https://leetcode.com/problems/length-of-last-word/
# April 1, 2024

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        notSpace = False
        length = 0

        for i in s[::-1]:
            if i != " ":
                notSpace = True
                length += 1
            elif i == " " and notSpace:
                break
            elif i != " ":
                length += 1
        
        return length
