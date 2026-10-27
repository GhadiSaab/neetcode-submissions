from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        sum_piles = 0
        res = max(piles)

        while l <= r: 
            mid = (l+r) // 2

            sum_piles = 0

            for pile in piles: 
                sum_piles += ceil(pile / mid)

            if sum_piles <= h: 
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1


        return res