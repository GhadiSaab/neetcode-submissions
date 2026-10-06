class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefixProduct = [1] * len(nums)
        sufixProduct = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            prefixProduct[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(len(nums)-1, -1, -1):
            sufixProduct[i] = suffix
            suffix *= nums[i]


        for i in range(len(prefixProduct)):
            prefixProduct[i] = prefixProduct[i] * sufixProduct[i]


        return prefixProduct



        