class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        left, right = 0, 1

        n = len(prices)

        #if ever right is less than left
        #then left = right
        #right += 1

        while right <= n-1:

            if prices[right] < prices[left]:
                left = right
                right += 1

                if right >= n:
                    break

            while right < n-2 and prices[right+1] > prices[right]:
                right += 1

            max_profit = max(max_profit, prices[right]-prices[left])

            right += 1

        return max_profit