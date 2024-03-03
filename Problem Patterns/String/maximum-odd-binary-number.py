# Problem Link: https://leetcode.com/problems/maximum-odd-binary-number

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        hashTable = Counter(list(s))

        return '1' * (hashTable['1'] - 1) + '0' * hashTable['0'] + '1' 
