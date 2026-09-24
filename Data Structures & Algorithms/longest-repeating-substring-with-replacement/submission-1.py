class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_count = {}
        l = 0
        maxlen = 0

        for r in range(len(s)):
            freq_count[s[r]] = 1 + freq_count.get(s[r], 0)

            while (r - l + 1) - max(freq_count.values()) > k:
                freq_count[s[l]] -= 1
                l += 1

            maxlen = max(maxlen, (r - l + 1))

        return maxlen 