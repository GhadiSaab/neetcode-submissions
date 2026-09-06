class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while right > left:
                total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if total == 0:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left-1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right+1]:
                        right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return res