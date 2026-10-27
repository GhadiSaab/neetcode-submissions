class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        count = 0 
        currentSum = 0

        for i in range( len(nums)):

            currentSum += nums[i]

            if (currentSum - k) in prefixSum:
                count += prefixSum[(currentSum - k)] 

            prefixSum[currentSum] = prefixSum.get(currentSum, 0) + 1

        return count



            