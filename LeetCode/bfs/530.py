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
            values.append(node.val)
            inorder(node.right)

        values = []

        inorder(root)

        answer = min([cur - prev for cur, prev in zip(values[1:], values[:-1])])

        return answer
