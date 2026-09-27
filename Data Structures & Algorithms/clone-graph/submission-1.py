"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        copynode = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            for _ in range(len(queue)):
                no = queue.popleft()

                for nei in no.neighbors:
                    if nei not in copynode:
                        copynode[nei] = Node(nei.val)
                        queue.append(nei)
                    copynode[no].neighbors.append(copynode[nei])


        return copynode[node]