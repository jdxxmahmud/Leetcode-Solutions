# Problem Link: https://leetcode.com/problems/maximum-score-after-splitting-a-string

class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0

        for char in s:
            if char == "1":
                ones += 1

        maxCount = 0

        for i in range(0, len(s) - 1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1

            maxCount = max(zeros + ones, maxCount)

        return maxCount
