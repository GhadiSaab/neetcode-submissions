class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }
        path = []
        res = []
        n = len(digits)

        if digits == '':
            return []

        def backtracking(index):
            if index == n:
                res.append(''.join(path[:]))
                return

            for ch in letters[digits[index]]:
                path.append(ch)
                backtracking(index+1)
                path.pop()

        backtracking(0)

        return res

            


