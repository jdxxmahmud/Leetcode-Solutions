# Problem Link: https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        len1, len2 = len(word1), len(word2)
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            if i < len1:
                res += word1[i]
                i += 1
            if j < len2:
                res += word2[j]
                j += 1
        
        return res
