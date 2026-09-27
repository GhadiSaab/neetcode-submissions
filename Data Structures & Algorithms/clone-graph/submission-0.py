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
        copynode = {}

        def dfs(node):
            if node in copynode:
                return copynode[node]

            copynode[node] = Node(node.val)

            for nei in node.neighbors:
                copynode[node].neighbors.append(dfs(nei))
            return copynode[node]

        if not node:
            return None
        return dfs(node)         