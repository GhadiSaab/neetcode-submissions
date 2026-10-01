from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def stairs(i):

            if i == n: return 1
            if i > n: return 0

            return stairs(i+1) + stairs(i+2)


        return stairs(0)
