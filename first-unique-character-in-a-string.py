# Problem Link: https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:

        hash = {}

        for i, char in enumerate(s):
            if char not in hash:
                hash[char] = i
            else:
                hash[char] = -1

        for idx in list(hash.values()):
            if idx != -1:
                return idx

        return -1 
