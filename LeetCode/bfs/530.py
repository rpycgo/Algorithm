# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.answer = min(self.answer, node.val-self.prev)
            self.prev = node.val

            inorder(node.right)

        self.prev = None
        self.answer = float('inf')

        inorder(root)

        return self.answer
