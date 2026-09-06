class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for num in nums: 
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        sorted_freq = sorted(freq, key=freq.get, reverse=True)

        for i in range(k):
            res.append(sorted_freq[i])

        return res
