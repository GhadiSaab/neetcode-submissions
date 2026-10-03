class Solution:
    from collections import deque
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) #frequency counter 
        maxHeap = []
        q = deque()
        time = 0

        for i in count.values():
            heapq.heappush(maxHeap, -i)

        while maxHeap or q: 
            time += 1
            if maxHeap:
                item = heapq.heappop(maxHeap)

                if item +1 != 0:
                    q.append((item+1, time+n))

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time 


        



