class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []
        nums.sort()

        def backtracking(start): 
            res.append(path[:])
            prev = 21

            for i in range(start, len(nums)):
                if prev == nums[i]:
                    continue

                path.append(nums[i])
                backtracking(i+1)
                path.pop()

                prev = nums[i]

            
        backtracking(0)

        return res