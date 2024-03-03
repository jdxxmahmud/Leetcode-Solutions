# Problem Link: https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        first, last = 0, len(nums) - 1

        res = []
        while first <= last:
            if first == last:
                res.append(nums[first] ** 2)
                break

            if abs(nums[first]) < abs(nums[last]):
                res.append(nums[last] ** 2)
                last -=1
            else:
                res.append(nums[first] ** 2)
                first += 1
        
        return res[::-1]
