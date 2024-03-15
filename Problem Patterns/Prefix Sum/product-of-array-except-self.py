# Problem Link: https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zerCount = 0
        for num in nums:
            if num != 0:
                prod *= num
            else:
                zerCount += 1

        res = []

        for num in nums:
            if num == 0:
                if zerCount == 1:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                if zerCount != 0:
                    res.append(0)
                else:
                    res.append(prod // num)

        return res

        
