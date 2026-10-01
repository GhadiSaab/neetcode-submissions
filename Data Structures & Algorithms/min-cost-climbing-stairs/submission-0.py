class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = cost[-2]
        b = cost[-1]
        n = len(cost)

        for i in range(n-3,-1,-1):
            a,b = cost[i] + min(a,b), a
        
        return min(a,b)