class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0 

        for i,num in enumerate(nums):

            if max_jump < i: 
                return False

            max_jump = max(i + num, max_jump)
        return True 