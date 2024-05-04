# Problem Link: https://leetcode.com/problems/boats-to-save-people

May 4, 2024

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        res = 0

        hi, lo = len(people) - 1, 0

        while lo <= hi:
            if people[lo] + people[hi] > limit:
                if people[hi] <= limit:
                    res += 1
                hi -= 1
            else:
                lo += 1
                hi -= 1
                res += 1

        return res
