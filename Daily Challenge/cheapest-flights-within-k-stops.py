# Problem Link: https://leetcode.com/problems/cheapest-flights-within-k-stops
# Feb 23, 2024

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n

        prices[src] = 0


        for _ in range(k + 1):
            temp = prices.copy()

            for src, dest, price in flights:

                if prices[src] == float("inf"):
                    continue
                    
                if temp[dest] > prices[src] + price:
                    temp[dest] = prices[src] + price

            prices = temp

        return -1 if prices[dst] == float("inf") else prices[dst]
