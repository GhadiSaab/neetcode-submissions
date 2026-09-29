# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        
        maxdepth = [0]

        def dfs(node,depth):

            if node is None:
                return depth

            maxdepth[0] = max(maxdepth[0],depth) 

            dfs(node.left,depth+1)
            dfs(node.right,depth+1)


        dfs(root,1)

        return maxdepth[0]


