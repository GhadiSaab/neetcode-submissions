class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = 0
        result = []
        for c in s:
            if c.isalnum():
                result.append(c.lower())
        stripped_s = ''.join(result)
        left = len(stripped_s) - 1

        while right < left:
            if stripped_s[right] != stripped_s[left]:
                return False
            right += 1
            left -= 1

        return True
             