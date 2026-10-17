class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        curSum = 0
        res = 0

        for i in range(len(nums)):
            curSum += nums[i]

            if (curSum - k) in prefixSum:
                res += prefixSum[(curSum-k)]
                

            prefixSum[curSum] = prefixSum.get(curSum,0) + 1


        return res




