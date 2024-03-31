## Problem Link: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hi, lo = 0, 0

        hash = {}
        res = 0

        for hi in range(len(nums)):
            if nums[hi] not in hash:
                hash[nums[hi]] = 1
            else:
                hash[nums[hi]] += 1

            if hash[nums[hi]] > k:
                # print(f"Oops {nums[lo:hi + 1]}")
                while lo < hi and hash[nums[hi]] > k:
                    hash[nums[lo]] -= 1
                    lo += 1
            else:
                # print(f"Yay {nums[lo:hi + 1]}")
                res = max(res, hi - lo + 1)

        return res
