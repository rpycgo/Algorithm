# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def inorder(node, depth):
            if not node:
                depths.append(depth)
                return

            inorder(node.left, depth+1)
            inorder(node.right, depth+1)

        depths = []

        inorder(root, 0)

        max_depth = max(depths)

        return max_depth
