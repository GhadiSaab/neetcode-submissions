# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 

        def dfs(node, curMax): 
            nonlocal count

            if node is None:
                return
            
            if node.val >= curMax:
                count += 1

            dfs(node.left, max(node.val,curMax))
            dfs(node.right, max(node.val,curMax))

        dfs(root,root.val)

        return count
        