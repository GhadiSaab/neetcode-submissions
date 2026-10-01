# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same(p,q):
            if p is None and q is None: return True
            if p is None or q is None: return False

            if p.val != q.val:
                return False

            return is_same(p.left,q.left) and is_same(p.right,q.right)
            

        def dfs(node):
            if node is None:
                return False

            if node.val == subRoot.val:
                if is_same(node,subRoot):
                    return True
            
            return dfs(node.left) or dfs(node.right)


        return dfs(root)
            

