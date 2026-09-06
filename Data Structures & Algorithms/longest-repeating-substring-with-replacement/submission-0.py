class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # How many times each letter appears in the CURRENT window [l, r]
        freq = {}

        left = 0
        best_length = 0
        most_common_count = 0  # highest single-letter count seen in any window so far

        for right in range(len(s)):
            current_char = s[right]

            # Step 1: add s[right] into the window's frequency count
            if current_char not in freq:
                freq[current_char] = 0
            freq[current_char] += 1

            # Step 2: update how big the biggest letter-group is
            most_common_count = max(most_common_count, freq[current_char])

            # Step 3: work out the window size right now
            window_length = right - left + 1

            # Step 4: how many letters in this window are "wrong" (not the majority letter)?
            letters_needing_replacement = window_length - most_common_count

            # Step 5: if that's more than we're allowed to fix, shrink from the left
            if letters_needing_replacement > k:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1

            # Step 6: record the best window length seen so far
            window_length = right - left + 1
            best_length = max(best_length, window_length)

        return best_length