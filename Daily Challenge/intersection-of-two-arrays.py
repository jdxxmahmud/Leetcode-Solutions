# Problem Link: https://leetcode.com/problems/intersection-of-two-arrays
# Daily Question - March 10, 2024

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(list(set(nums1)))
        nums2 = sorted(list(set(nums2)))
        
        res = []

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1 
            else:
                i +=1

        return res
