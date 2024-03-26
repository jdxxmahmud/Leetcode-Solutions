# Problem Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            val = abs(num)

            if nums[val - 1] > 0:
                nums[val - 1] *= -1
            # print(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)


        return res

