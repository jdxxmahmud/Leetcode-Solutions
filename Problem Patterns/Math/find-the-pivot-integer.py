# Problem Link: https://leetcode.com/problems/find-the-pivot-integer

class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n * (n + 1) // 2)
        return int(x) if int(x) == x else -1
