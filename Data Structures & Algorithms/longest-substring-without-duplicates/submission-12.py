
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        window = set()
        maxsub = 0

        while r < len(s): 

            if s[r] not in window:
                window.add(s[r])
                r += 1

            else:
                while s[r] in window:
                    window.discard(s[l])
                    l += 1

            maxsub = max(r-l, maxsub)


        return maxsub
            
                

 



