# Problem Link: https://leetcode.com/problems/maximum-strong-pair-xor-i

class Solution:

    def isStrong(self, x, y):
        return abs(x - y) <= min(x, y)


    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
        maxXor = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if self.isStrong(nums[i], nums[j]):
                    maxXor = max(maxXor, nums[i] ^ nums[j])
        
        return maxXor
