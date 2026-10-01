class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            if abs(left - right) > 1:
                balanced[0] = False

            return 1 + max(left, right)

        height(root)
        return balanced[0]