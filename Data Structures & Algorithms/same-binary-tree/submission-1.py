# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        valid = [True]

        if p is None and q is None : return True
        if p is None and q is not None: return False
        if p is not None and q is None: return False

        if p.val != q.val:
            return False

        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return
            if node1 is None or node2 is None:
                valid[0] = False
                return

            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)

            if node1.left or node2.left:
                if node1.left is None or node2.left is None or node1.left.val != node2.left.val:
                    valid[0] = False
                    return

            if node1.right or node2.right:
                if node1.right is None or node2.right is None or node1.right.val != node2.right.val:
                    valid[0] = False
                    return

        dfs(p, q)

        return valid[0]




