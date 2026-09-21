# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None: return []
        
        q = deque()
        q.append((root,0))
        res = [[]]
        res2 = []

        while q:

            node,level = q.popleft()

            if level == len(res):
                res.append([])

            res[level].append(node.val)

            if node.left:
                q.append((node.left, level+1))

            if node.right:
                q.append((node.right, level+1))

        for i in res: 
            res2.append(i[-1])

        return res2
        

            
