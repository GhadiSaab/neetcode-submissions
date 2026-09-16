# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None : return root 

        def dfs(root): 
            if root is None:
                return 
            
            node = root
            node.left,node.right = node.right,node.left

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return root 

