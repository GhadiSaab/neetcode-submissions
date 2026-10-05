class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pmin = pmax = maxi = nums[0]

        for i in range(1,len(nums)):
            candidates = (pmax * nums[i], pmin* nums[i], nums[i])
            pmax = max(candidates)
            pmin = min(candidates)

            maxi = max(maxi,pmax)


        return maxi 

            