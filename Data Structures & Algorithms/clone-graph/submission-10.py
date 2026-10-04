"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    from collections import deque
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        first = node

        nodes = {}
        nodes[node] = Node(node.val)
        q = deque([node])

        while q:
            node = q.popleft()
            for nei in node.neighbors:
                if nei not in nodes:
                    q.append(nei)
                    nodes[nei] = Node(nei.val)

        for nodess in nodes: 
            for nei in nodess.neighbors:
                nodes[nodess].neighbors.append(nodes[nei])

        return nodes[first]
        

        