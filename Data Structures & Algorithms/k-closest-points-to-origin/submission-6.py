class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math 
        heap = []
        for x,y in points: 
            distance = math.sqrt((x)**2 + (y)**2)
            heapq.heappush(heap, (-distance,[x,y]))

        while len(heap) > k: 
            heapq.heappop(heap)

        return [point for _, point in heap]