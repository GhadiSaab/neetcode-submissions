class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res =[]

        def is_palindrom(s):
            if len(s) == 1:
                return True

            l,r = 0,len(s)-1

            while l < r:
                if s[l] != s[r]:
                    return False
                l +=1
                r -=1
            return True

            
        def backtracking(i):
            if i >= len(s):
                res.append(path[:])
                return


            for j in range(i, len(s)):
                if is_palindrom(s[i:j+1]):
                    path.append(s[i:j+1])
                    backtracking(j+1)
                    path.pop()


        backtracking(0)
        return res



            


            
