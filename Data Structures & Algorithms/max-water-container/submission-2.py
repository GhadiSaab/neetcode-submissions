class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end  = 0, len(heights) -1 

        maxWater = float('-inf')

        while start < end: 

            water = min(heights[start], heights[end]) * (end - start)

            if  heights[start] < heights[end]: 
                start += 1
            else:
                end -= 1


            maxWater = max(maxWater, water)

        return maxWater

