class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res =[]
        total = 0

        def backtrack(index,total):
            if total > target:
                return 
            if total == target:
                res.append(path[:])
                return 
            
            for i in range(index,len(nums)):
                path.append(nums[i])
                backtrack(i, total + nums[i])
                path.pop()



        backtrack(0,0)
        return res 
