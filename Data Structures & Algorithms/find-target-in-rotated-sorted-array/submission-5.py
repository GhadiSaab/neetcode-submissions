class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1 
        while l < r:
            mid = (l+r) // 2 
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        # l,r should have the index of the minimmum value. whch is the num of rotation
        min_index = l
        max_index = l-1
        if target >= nums[0] and target <= nums[max_index]:
            i_l = 0
            i_r = max_index
        else:
            i_l = min_index
            i_r = len(nums) - 1 

        if min_index == 0:
            i_l = 0
            i_r = len(nums) -1 
        
        while i_l <= i_r: 
            i_mid = (i_l + i_r) // 2
            if nums[i_mid] == target:
                return i_mid
            elif nums[i_mid] < target:
                i_l = i_mid + 1
            else:
                i_r = i_mid - 1


        return -1


