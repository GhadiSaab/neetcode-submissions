class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            currentA = min(heights[l],heights[r]) * (r - l)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
            
            maxA = max(maxA,currentA)

        return maxA
