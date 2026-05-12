class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxp = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                p = prices[right] - prices[left]
                maxp = max(p, maxp)
            else:
                left = right
            right += 1

        return maxp