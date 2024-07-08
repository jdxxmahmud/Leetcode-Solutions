# Problem Link: https://leetcode.com/problems/valid-perfect-square/

class Solution {
        public boolean isPerfectSquare(int num) {
        if (num == 1) {
            return true;
        }

        long lo = 0, hi = num;

        while (lo <= hi) {
            long mid = (hi + lo) / 2;
            if (mid == hi || mid == lo) {
                break;
            }

            if (mid * mid == num) {
                return true;
            } else if (mid * mid > num) {
                hi = mid;
            } else {
                lo = mid;
            }
        }

        return false;
    } 
}
