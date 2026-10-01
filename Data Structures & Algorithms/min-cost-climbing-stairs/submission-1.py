from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        @cache
        def price(i):
            if i >= n:
                return 0
            
            return cost[i] + min(price(i+1), price(i+2))

    
        return min(price(0), price(1))