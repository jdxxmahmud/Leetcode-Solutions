# Problem Link: https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return True
        
        lo, hi = 0, num

        while lo <= hi:

            mid = (hi + lo) // 2
            if mid == hi or mid == lo:
                break

            # print(lo, hi, mid, mid * mid,  num)/

            if mid * mid == num:
                return True
            elif mid * mid > num:
                hi = mid
            else:
                lo = mid

        return False
