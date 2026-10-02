class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def comb2(start,total):
            if total > target:
                return 
            if total == target:
                res.append(path[:])

            prev = -1

            for i in range(start, len(candidates)):
                if prev == candidates[i]:
                    continue
                path.append(candidates[i])
                comb2(i+1, total + candidates[i])
                path.pop()

                prev = candidates[i]

            
        comb2(0,0)

        return res