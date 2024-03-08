# Problem Link: https://leetcode.com/problems/count-elements-with-maximum-frequency
# March 8, 2024

class Solution:

    def get_freq_tab(self, nums: List[int]) -> dict:
        hashTab = {}
        for num in nums:
            if num in hashTab:
                hashTab[num] += 1
            else:
                hashTab[num] = 1

        return hashTab

    def maxFrequencyElements(self, nums: List[int]) -> int:

        freq_tab = self.get_freq_tab(nums)
        freq_freq = self.get_freq_tab(freq_tab.values())

        max_freq = max(freq_freq.keys())

        return freq_freq[max_freq] * max_freq
         
