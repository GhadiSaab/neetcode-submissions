class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def comb(start, total):
            if total > target: return 
            if total == target:
                res.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                comb(i, total+ nums[i]) 
                path.pop()

            
        comb(0,0)
        return res