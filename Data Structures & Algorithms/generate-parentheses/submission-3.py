class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        path = []

        def backtracking(closed, opened):
            if len(path) == 2*n:
                res.append(''.join(path[:]))
                return 

            if opened < n:
                path.append('(')
                backtracking(closed,opened+1)
                path.pop()

            if opened > closed:
                path.append(')')
                backtracking(closed+1, opened)
                path.pop()


        backtracking(0,0)
        return res

            

            