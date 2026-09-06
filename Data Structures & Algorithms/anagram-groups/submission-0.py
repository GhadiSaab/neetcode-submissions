class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}

        for s in strs:
            count = 26 * [0]
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
                
            key = tuple(count)
            
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)

        for key in hashmap:
            result.append(hashmap[key])

        return result