class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        for s in strs:
            anagram = [0] * 26
            for char in s: 
                anagram[ ord(char) - ord('a') ] += 1

            anagram = tuple(anagram)
            if anagram not in hashmap:

                hashmap[anagram] = []

            hashmap[anagram].append(s)


        return list(hashmap.values())
