from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < l:
                l = prices[i]
            else:
                if (prices[i] - l) > profit:
                    profit = prices[i] - l
        return profit
