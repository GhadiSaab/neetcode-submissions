class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        
        l, r = 0, len(s1)
        count_s1 = {}
        count = {}

        for i in range(r):
            count_s1[s1[i]] = count_s1.get(s1[i], 0) + 1 
            count[s2[i]] = count.get(s2[i], 0) + 1

        for r in range(r,len(s2)):
            if count_s1.items() == count.items():
                return True

            count[s2[l]] -= 1
            if count[s2[l]] == 0:
                del count[s2[l]]
            l += 1
            count[s2[r]] = 1 + count.get(s2[r],0)

        return count_s1.items() == count.items()


            