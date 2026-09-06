class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            if prices[r] - prices[l] > profit:
                profit = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
            r += 1
        
        return profit


#  prices=[2,1,2,1,0,1,2]
# l = 0, r = 1, prfit = 0

