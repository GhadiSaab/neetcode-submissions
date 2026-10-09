class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        numIntervals = 0
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start < res[-1][1]:
                res[-1][1] = min(end,res[-1][1])
                numIntervals += 1
            else:
                res.append([start,end])


        return numIntervals