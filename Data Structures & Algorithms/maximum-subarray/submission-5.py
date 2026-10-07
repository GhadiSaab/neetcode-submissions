class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        cur = nums[0]

        for i in nums[1:]:
            cur = max(i,cur+i)
            best = max(best, cur)

        return best