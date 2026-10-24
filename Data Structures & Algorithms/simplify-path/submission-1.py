class Solution:
    def simplifyPath(self, path: str) -> str:
        spath = path.split('/')  
        stack = []

        for dirname in spath:
            if dirname == '' or dirname == '.':
                continue
            elif dirname == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dirname)

        return '/' + '/'.join(stack)