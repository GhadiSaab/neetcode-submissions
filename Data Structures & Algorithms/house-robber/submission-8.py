from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def best(i):
            if i == 0:
                return nums[0]

            if i==1:
                return max(nums[0],nums[1])

            return max(best(i-1), best(i-2) + nums[i])

        return best(len(nums)-1)