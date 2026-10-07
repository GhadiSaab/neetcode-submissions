class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums)+1)]
        res = []

        for i in nums:
            freq[i] = freq.get(i,0) + 1

        for val, freq in freq.items():
            bucket[freq].append(val)

        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res
