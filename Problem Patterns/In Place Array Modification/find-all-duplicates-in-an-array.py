# Problem Link: https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            # print(f"num: {num}\tres: {res} \tnums{nums}")
            num = abs(num)

            if nums[num-1] < 0:
                res.append(num)

            nums[num - 1] = -nums[num - 1]


        return res
