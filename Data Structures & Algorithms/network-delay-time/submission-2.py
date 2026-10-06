import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:



        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        dist = [float('inf')] * (n + 1)   # n+1 because nodes are 1-indexed
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:             # stale entry
                continue
            for nei, t in adj[node]:
                nd = d + t
                if nd < dist[nei]:         # relaxation
                    dist[nei] = nd
                    heapq.heappush(heap, (nd, nei))

        ans = max(dist[1:])
        return ans if ans < float('inf') else -1

