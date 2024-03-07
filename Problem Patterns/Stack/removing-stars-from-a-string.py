# Problem Link: https://leetcode.com/problems/removing-stars-from-a-string

class Solution:
    def removeStars(self, s: str) -> str:
        q = deque()

        for char in s:
            if char != '*':
                q.append(char)
            else:
                q.pop()

        return "".join(list(q))
