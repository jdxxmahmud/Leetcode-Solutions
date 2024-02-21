# Problem Link: https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        l = bin(left)[2:]
        r = bin(right)[2:]

        if len(l) != len(r):
            l = (len(r) - len(l)) * '0' + l

        res = ""

        for i in range(len(r)):
            if l[i] != r[i]:
                res += (len(r) - i) * '0'
                break

            res += l[i]

        return int(res, 2)
