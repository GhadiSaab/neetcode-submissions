"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        curr = head

        while curr:
            nodes[curr] = Node(curr.val,curr.next,curr.random)
            curr = curr.next

        curr = head

        if curr:
            head2 = nodes[curr]
        else:
            return head

        while curr:
            if curr.next:
                nodes[curr].next = nodes[curr.next]
            else:
                nodes[curr].next = None


            if curr.random:
                nodes[curr].random = nodes[curr.random]
            else:
                nodes[curr].random = None

            curr = curr.next

        return head2

