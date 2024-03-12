# Problem Link: https://leetcode.com/problems/custom-sort-string

class Solution:
    def makePositions(self, order: str):
        posHash = {}
        for i, char in enumerate(order):
            posHash[char] = i

        return posHash

    def customSortString(self, order: str, s: str) -> str:
        posHash = self.makePositions(order)
        resArr = [""] * (len(order) + 1)

        for char in s:
            if char in posHash:
                resArr[posHash[char]] += char
            else:
                resArr[len(order) - 1] += char

        return "".join(resArr)
