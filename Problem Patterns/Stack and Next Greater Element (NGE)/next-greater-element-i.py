# https://leetcode.com/problems/next-greater-element-i/

class Solution:

    def NEGmap(self, nums):

        hashMap = {}

        stack = []

        for i in range(len(nums) - 1, -1, -1):

            if stack:
                while stack:
                    if stack[-1] > nums[i]:
                        hashMap[nums[i]] = stack[-1]
                        stack.append(nums[i])
                        break
                    else:
                        stack.pop()

            if not stack:
                hashMap[nums[i]] = -1
                stack.append(nums[i])

        return hashMap

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        lookerTable = self.NEGmap(nums2)

        res = []

        for num in nums1:
            res.append(lookerTable[num])

        return res
