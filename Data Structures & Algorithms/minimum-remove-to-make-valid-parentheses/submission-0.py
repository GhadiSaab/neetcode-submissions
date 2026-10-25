class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        bad = set()
        for index, char in enumerate(s): 

            if char == '(':
                stack.append((index,char))

            elif char == ')':

                if stack and stack[-1][1] == '(':
                    stack.pop()
                else:
                    stack.append((index,char)) 

        
        for index, char in stack: 
            bad.add(index)

        res = ''
        for index, char in enumerate(s):
            if index not in bad: 
                res += char

        return res



