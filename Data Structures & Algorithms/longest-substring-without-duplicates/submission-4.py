from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        l = 0
        r = 1
        max_sub = 1
        window = set()
        window.add(s[l])
            
        while r < len(s):
            if s[r] in window:
                if window:
                    window.remove(s[l])
                l += 1
            else:
                window.add(s[r])
                r += 1
            
            max_sub = max((len(window),max_sub))
            
        return max_sub






