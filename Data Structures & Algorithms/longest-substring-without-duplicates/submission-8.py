class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0

        start, end = 0,0
        string = set()

        while end < len(s): 


            if s[end] not in string:
                string.add(s[end])
                end += 1
            else: 
                string.discard(s[start])
                start += 1

            maxlen = max(maxlen, len(string))

        return maxlen 
