# Problem Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        outParen = False
        Inner = 0
        res = ""

        for brac in s:
            if outParen == False:
                if brac == "(":
                    outParen = True
            else:
                if brac == "(":
                    Inner += 1
                    res += brac
                else:
                    if Inner > 0:
                        Inner -= 1
                        res += brac
                    else:
                        outParen = False
            # print(f"brac: {brac}, outParen: {outParen}, Inner: {Inner}, res: {res}")

        return res
