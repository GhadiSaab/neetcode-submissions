class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = nums[0]

        # finding if there is a cycle (guarenteed)
        while True:
            s = nums[s]
            f = nums[nums[f]]

            if s == f: break

        f = nums[0]
        while f != s:
            f = nums[f]
            s = nums[s]

        return s