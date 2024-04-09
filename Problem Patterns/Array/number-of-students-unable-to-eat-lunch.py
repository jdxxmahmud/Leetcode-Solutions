# Problem Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stHash = defaultdict(int)
        for i in students:
            stHash[i] += 1
        st = len(students)

        for sd in sandwiches:
            if stHash[sd]:
                st -= 1
                stHash[sd] -= 1
            else:
                return st

        return st
