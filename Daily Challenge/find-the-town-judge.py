# Problem Link: https://leetcode.com/problems/find-the-town-judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n == 1: return 1

        trustedHash = {}
        trustingHash = {}

        for trusting, trusted in trust:
            trustedHash[trusted] = trustedHash.get(trusted, 0) + 1
            trustingHash[trusting] = trustingHash.get(trusting, 0) + 1

        for key, val in trustedHash.items():
            if val == n - 1 and key not in trustingHash:
                return key

        return -1
        
