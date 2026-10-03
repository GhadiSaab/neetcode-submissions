class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = [False] * len(nums)

        def backtrack(index):
            res.append(path[:])

            for i in range(index,len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(i)
                    used[i] = False
                    path.pop()


        backtrack(0)
        return res
