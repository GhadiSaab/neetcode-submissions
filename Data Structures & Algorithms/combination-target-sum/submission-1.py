class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        total = 0
        res = []

        def dfs(start,total):
            if total > target: return
            if total == target:
                res.append(path[:])
                return

            for i in range(start,len(nums)):
                path.append(nums[i])   
                dfs(i, total+nums[i])
                path.pop()

        dfs(0,0)

        return res