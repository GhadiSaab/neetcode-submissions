class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path = []
        res = []

        def backtrack(start,total):
            if total > target:
                return 
            if total == target:
                res.append(path[:])
                return 

            prev = -1
            for i in range(start,len(candidates)):
                if prev == candidates[i]:
                    continue
                
                prev = candidates[i]
                path.append(candidates[i])
                backtrack(i+1, total + candidates[i])
                path.pop() 

        backtrack(0,0)

        return res