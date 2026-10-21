from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []        
        freq_dist = Counter(nums)
        res = []

        for element,freq in freq_dist.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, element))

            else:
                if freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq,element))


        while heap:
            freq,element = heapq.heappop(heap)
            res.append(element)

        return res





        