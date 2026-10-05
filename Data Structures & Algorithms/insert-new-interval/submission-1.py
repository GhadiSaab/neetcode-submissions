class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_st,new_end = newInterval
        i = 0

        while i < len(intervals) and new_st > intervals[i][1]:
            i += 1
        
        while i < len(intervals) and new_end >= intervals[i][0]:
            new_st = min(new_st, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            intervals.pop(i)

        
        intervals.insert(i,[new_st,new_end])
        return intervals



