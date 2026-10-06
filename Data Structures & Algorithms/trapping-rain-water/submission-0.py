class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * len(height)
        right = [0] * len(height)
        mid= [0] * n 
        water = 0

        b = 0

        for i in range(n):
            b = max(height[i],b)
            left[i] = b

        b = 0
        for i in range(n-1, -1, -1):
            b =  max(height[i],b)
            right[i] = b

        for i in range(n):
            mid[i] = min(left[i], right[i]) - height[i]

        for i in range(n):
            water += mid[i]


        return water
        

        

        