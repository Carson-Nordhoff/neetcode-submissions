class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        left, right = 0, 1

        n = len(prices)

        while right < n:

            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return max_profit