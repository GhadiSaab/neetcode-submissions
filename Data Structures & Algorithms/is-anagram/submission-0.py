class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for string in s:
            hashmap1[string] = hashmap1.get(string,0) + 1 
        for string in t:
            hashmap2[string] = hashmap2.get(string,0) + 1
        return hashmap1 == hashmap2


        

        