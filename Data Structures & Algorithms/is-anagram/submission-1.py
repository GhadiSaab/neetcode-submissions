class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        for string in s:
            hashmap1[string] = hashmap1.get(string,0) + 1 
        for string in t:
            hashmap1[string] = hashmap1.get(string,0) - 1
        for val in hashmap1.values():
            if val != 0:
                return False
        return True


        

        