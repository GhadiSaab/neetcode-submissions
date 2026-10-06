class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        sump =0
        res = r 

        while l<=r:

            k = (l+r) // 2
            sump = 0

            for pile in piles:
                sump += math.ceil(pile/k)

            if sump <= h: 
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1
        

        return res

            

            

