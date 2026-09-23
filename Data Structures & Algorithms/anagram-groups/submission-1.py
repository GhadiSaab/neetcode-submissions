class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        res = []

        for s in strs: 
            count = [0] * 26
            for c in s: 
                count[ord(c) - ord('a')] += 1

            count = tuple(count)
            if count in anagrams: 
                anagrams[count].append(s)
            else:
                anagrams[count] = [s]

        for i in anagrams.values():
            res.append(i)

        return res