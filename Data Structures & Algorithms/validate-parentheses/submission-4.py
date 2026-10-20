class Solution:
    def isValid(self, s: str) -> bool:
        test = {'[':']', "{":"}", '(' : ')'}
        stack = []

        if len(s) == 1 or len(s) == 0:
            return False


        for char in s: 
            if char in test:
                stack.append(char)
            else:
                if not stack or test[stack.pop()] != char:
                    return False

        if stack: 
            return False
        else:
            return True
            