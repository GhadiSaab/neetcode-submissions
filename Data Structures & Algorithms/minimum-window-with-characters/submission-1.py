class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing = len(t)
        need = Counter(t)
        l = 0
        best_start, best_len = 0, float('inf')

        for r, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1 #our junk

            if missing == 0: 

                while need[s[l]] < 0:
                    need[s[l]] += 1
                    l += 1

                if r - l + 1 < best_len:
                    best_start = l
                    best_len = r - l + 1

                need[s[l]] += 1
                l += 1
                missing += 1


        if best_len == float('inf'):
            return ''
        else:
            return s[best_start: best_start + best_len]

                

            

              