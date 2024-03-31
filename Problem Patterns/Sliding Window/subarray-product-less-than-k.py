# Problem Link: https://leetcode.com/problems/subarray-product-less-than-k

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        lo, hi = 0, 0
        res = 0

        prod = 1

        while hi < len(nums):
            prod *= nums[hi]

            while prod >= k and lo <= hi:
                prod = prod // nums[lo]
                lo += 1
            
            res += (hi - lo) + 1

            hi += 1


        return res
