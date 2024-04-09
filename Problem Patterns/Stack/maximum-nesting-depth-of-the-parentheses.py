# Problem Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        q = []
        curr = 0
        for char in s:
            if char == '(':
                q.append(char)
                curr += 1
                depth = max(curr, depth)
            elif char == ")":
                q.pop()
                curr -= 1

            # print(char, q, curr, depth)

        return depth
