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

        
        c = list(s)
        for index, char in stack: 
            c[index] = ''

        return ''.join(c)



