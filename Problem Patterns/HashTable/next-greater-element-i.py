# Problem Link: https://leetcode.com/problems/next-greater-element-i

class Solution:
    
    hashTable = {}

    def findElementsPosition(self, arr):

        for idx, num in enumerate(arr):
            self.hashTable[num] = idx
    
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        self.findElementsPosition(nums2)

        res = []

        for num in nums1:
            
            greaterFound = False
            startRange = self.hashTable[num]

            for j in range(startRange, len(nums2)):

                if nums2[j] > num:
                    res.append(nums2[j])
                    greaterFound = True
                    break
            if not greaterFound:
                res.append(-1)
        


        return res
