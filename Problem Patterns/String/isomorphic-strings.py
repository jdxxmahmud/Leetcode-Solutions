# Problem Link: https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sHash = {}
        tHash = {}

        for i in range(len(s)):
            if ((t[i] in sHash and s[i] != sHash[t[i]]) or
                (s[i] in tHash and tHash[s[i]] != t[i])):
                    return False

            sHash[t[i]] = s[i]
            tHash[s[i]] = t[i]

        return True
