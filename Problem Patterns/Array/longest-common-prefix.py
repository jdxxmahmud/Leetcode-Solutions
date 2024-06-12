# Problem Link: https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcp = strs[0]

        for i in range(1, len(strs)):
            # print(lcp, strs[i])
            temp = ''
            for j in range(len(strs[i])):
                if j == len(lcp) or strs[i][j] != lcp[j]:
                    break
                else:
                    temp += lcp[j]
            lcp = temp

        return lcp
