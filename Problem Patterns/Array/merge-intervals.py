# Problem Link: https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        inter = intervals[0]
        for i in range(1, len(intervals)):
            if  inter[1] >= intervals[i][0]:
                inter = [min(inter[0], intervals[i][0]), max(inter[1], intervals[i][1])]
            else:
                res.append(inter)
                inter = intervals[i]
            
        res.append(inter)
            

        return res
