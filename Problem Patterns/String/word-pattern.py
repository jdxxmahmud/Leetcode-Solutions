# Problem Link: https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sHash = {}
        pHash = {}
        if len(pattern) != len(s.split(" ")):
            return False

        for i, word in enumerate(s.split(" ")):
            if ((pattern[i] in pHash and pHash[pattern[i]] != word) or
                (word in sHash and sHash[word] != pattern[i])):
                print(i, word, pattern[i])
                return False
            else:
                pHash[pattern[i]] = word
                sHash[word] = pattern[i]

        return True
