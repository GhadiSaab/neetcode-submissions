# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root,float('-inf'))]
        gd_nodes = 0


        while stack:

            node,largest = stack.pop()

            if node.val >= largest:
                gd_nodes += 1

            largest = max(node.val,largest)

            if node.left: stack.append((node.left,largest))
            if node.right: stack.append((node.right, largest))

        return gd_nodes