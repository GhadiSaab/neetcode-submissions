class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dist = set(nums)
        maxi = 0

        for i in dist:
            if i-1 not in dist: 
                count = 1
                test = i
                while test in dist:
                    test += 1 
                    if test in dist: 
                        count += 1

                maxi = max(maxi,count)


        return maxi