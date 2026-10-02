class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        def subset(start):
            res.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                subset(i+1)
                path.pop()

        subset(0)
        return res 