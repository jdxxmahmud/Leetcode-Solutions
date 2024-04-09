# Problem Link: https://leetcode.com/problems/time-needed-to-buy-tickets
# April 9, 2024


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]

        res = 0

        for i, ticket in enumerate(tickets):
            if i <= k:
                res += min(target, ticket)
            else:
                res += min(target - 1, ticket)

            # print(ticket, res)
            
        return res
