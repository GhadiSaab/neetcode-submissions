from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res =0
        inf = float('inf')

        @cache
        def dfs(total): 
            if total == amount:
                return 0
            if total > amount:
                return inf

            best = inf

            for coin in coins:
                best = min(best, 1+dfs(total + coin))
            return best

        res = dfs(0)
        return -1 if res == inf else res

