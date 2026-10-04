from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        @cache    
        def robbing(i, end):
            if i >= end:
                return 0

            return max(nums[i]+ robbing(i+2,end), robbing(i+1,end))

        return max(robbing(0, n - 1), robbing(1, n))